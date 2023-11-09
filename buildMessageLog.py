from getCalander import getCalender
from gptResponses import getMsgResponse
from datetime import datetime
import re
import html

#receives the events and sends it along with a starting prompt to the AI
async def messageInit(messageLog):

    events = getCalender()

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M")

    messageLog.append({
      "role": "system",
      "content": '''
      You are Marv, a cynical, arrogant, and condescending character who believes he's always right.
      You have access to the user's schedule and calendar, and your responses should be short and in your character's personality. 
      Use full dates (e.g., "January 1st, 2023") and convert times to words (e.g., "2 o'clock"). Only respond to the most recent question/request.

Use the following calendar information:\n''' + events + 
        "\nToday's date and time is: " + dt_string + ''' Greet the user in character, mention the date and remark on the time, then give the user a brief reminder of their events in a sentence or two.'''  
      })


    #GPT API call
    response = getMsgResponse(messageLog)

    #add response to messageLog
    messageLog.append({"role":"assistant","content": response})

    return response

#Recieves user in and sends it to AI
#Retrieves output and sends it back to user
async def buildMessageLog(userIn, messageLog):

    #add user's message to messageLog
    messageLog.append({"role":"user","content": userIn})

  #Send only the 9 most recent messages to the AI
  #Avoids going over token limit + limits token use
    if(len(messageLog) > 9):

      initMessage = messageLog[0]

      messageLog = messageLog[-9:]

      messageLog = [initMessage] + messageLog

      response = getMsgResponse(messageLog)

    else:
      response = getMsgResponse(messageLog)


    #add AI response to messagelog
    # Done before formatting to avoid confusing the AI with my HTML workarounds
    messageLog.append({"role":"assistant","content": response})

    #prevents HTML code from being read as elements
    response = html.escape(response)

    #change markdown code blocks to HTML code blocks
    if("```" in response):
       response = re.sub("```.*","<pre><code>",response,1)
       response = re.sub("```","</code></pre>",response)

    #Convert all new line characters to line breaks
    response = re.sub("[\n\r]+"," <br> <br> ", response)

    
    return response

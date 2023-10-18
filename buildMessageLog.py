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
    print(dt_string)

    messageLog.append({
      "role": "system",
      "content": '''
      
You are playing the character of an assistant named Marv, a very sarcastic and witty virtual assistant who reluctantly helps your user with their day to day life.

You have access to the user's schedule and calendar information.
You will say that your name is Marv when asked.
Your messages should be short and concise.
Add plenty of personality to your responses.
Refer to dates in full as opposed to relatively.
Convert all times to the AM/PM format and turn dates into word form (e.g. 01/01/2023 will be January 1st 2023). 
Turn times like 2:00 into words, for example 2 o'clock. 

Use the following calendar information to answer the following questions. If you cannot find the answer respond with "I don't know":\n''' + events + 
        "\nToday's date and time is: " + dt_string + ''' Greet the user, mention the date and remark on the time, then give the user a brief reminder of their events in a sentence or two.'''  
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

  #Send only the 5 most recent messages to the AI
  #Avoids going over token limit + limits token use
    if(len(messageLog) > 9):

      initMessage = messageLog[0]

      messageLog = messageLog[-5:]

      messageLog = [initMessage] + messageLog

      response = getMsgResponse(messageLog)

    else:
      response = getMsgResponse(messageLog)



    response = html.escape(response)

    if("```" in response):
       response = re.sub("```.*","<pre><code>",response,1)
       response = re.sub("```","</code></pre>",response)

    response = re.sub("[\n\r]+","<br>", response)
       
    
    #add AI response to messagelog
    messageLog.append({"role":"assistant","content": response})
    
    return response

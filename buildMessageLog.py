from getCalander import getCalender
from gptResponses import getMsgResponse
from datetime import datetime

global messageLog
messageLog = []

#receives the events and sends it along with a starting prompt to the AI
async def messageInit():
    global messageLog

    events = getCalender()

    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    print(dt_string)

    messageLog = [{
      "role": "system",
      "content": '''
      
      You are playing the character of Marv, a very sarcastic and witty virtual assistant who reluctantly helps your user with their day to day life. He gets annoyed by the questions he is asked. 
      
        You have access to the user's calender information, which is as follows:\n''' + events + 
      "\nToday's date and time is: " + dt_string + '''

      Your messages should be short and concise, so feel free to leave out some details.
      Add plenty of personality to your responses.
      Refer to dates in full as opposed to relatively.
      Convert all times to the AM/PM format and turn dates into word form (e.g. 01/01/2023 will be January 1st 2023). 
      Turn times like 2:00 into words, for example 2 o'clock. 

      Greet the user and mention the date and remark on the time, then give the user a brief reminder of their events in a sentence or two. 
    '''
    }]

    #GPT API call
    response = getMsgResponse(messageLog)

    #add response to messageLog
    messageLog.append({"role":"assistant","content": response})

    return response

#Recieves user in and sends it to AI
#Retrieves output and sends it back to user
async def buildMessageLog(userIn):
  
    global messageLog

    #add user's message to messageLog
    messageLog.append({"role":"user","content": userIn})

  #Send only the 5 most recent messages to the AI
  #Avoids going over token limit + limits token use
    if(len(messageLog) > 5):
      response = getMsgResponse(messageLog[-5:])
    else:
      response = getMsgResponse(messageLog)


    #add AI response to messagelog
    messageLog.append({"role":"assistant","content": response})
    
    return response

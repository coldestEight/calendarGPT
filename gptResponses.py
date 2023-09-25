from os import environ as env
import openai
import dotenv

dotenv.load_dotenv()
openai.api_key = env["OPENAI_API_KEY"]

def getMsgResponse(messageLog):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messageLog, temperature=1,max_tokens=300)
    rawOut = response.choices[0].message.content

    punctuationList = [".","?","!"]
    cutoffPos = 0
    for i in range(len(rawOut)):
        if rawOut[i] in punctuationList:
            cutoffPos = i

    return rawOut[0:cutoffPos+1]


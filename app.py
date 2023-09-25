import asyncio
from flask import Flask, render_template,send_file, jsonify, request

app = Flask(__name__)

#display main page
@app.route('/')
def index():
    return render_template('index.html')

#initialize first message from AI
@app.route('/run_init', methods=['POST'])
def runInit():
    from buildMessageLog import messageInit
    response = asyncio.run(messageInit())
    #send response back to webpage as json
    return jsonify({'response' : response})

#get user message from webpage
@app.route('/get_message', methods=['POST'])
def getMessage():
    from buildMessageLog import buildMessageLog
    #read in user input from json
    userInJSON = request.get_json()
    response = asyncio.run(buildMessageLog(userInJSON["userIn"]))
    #send response back as json
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)

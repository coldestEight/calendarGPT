import asyncio
from flask import Flask, render_template,send_file, jsonify, request


cwd = "C:/Users/khans/Desktop/Projects/calanderGPT"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/templates/subpage.html')
def subpage():
    return send_file(cwd + "/templates/subpage.html")

@app.route('/run_init', methods=['POST'])
def runInit():
    from buildMessageLog import messageInit
    response = asyncio.run(messageInit())
    return jsonify({'response' : response})

@app.route('/get_message', methods=['POST'])
def getMessage():
    from buildMessageLog import buildMessageLog
    userInJSON = request.get_json()
    response = asyncio.run(buildMessageLog(userInJSON["userIn"]))
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
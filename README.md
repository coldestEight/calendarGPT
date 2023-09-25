# calendarGPT
Virtual assistant with access to calendar events using Google Calendar.

# Getting Started

## Dependencies 
 - Flask
 - Open AI Python Library
 - Google API Libraries

## Requirements
 - Google OAuth 2.0 Client ID (credentials.json)
 - OpenAI API key (put in .env)

## Setup
1. Clone this repo
```
git clone https://github.com/coldestEight/calendarGPT.git
```
2. Get Google API Key. See [this guide](https://developers.google.com/workspace/guides/create-credentials).

3. Get OpenAI API Key
   - Make an OpenAI developer account
   - Generate API key
   - Put in .env file like so:
  ```
OPENAI_API_KEY = <insert_your_key_here>
```

4. Install all dependency libraries
   - Flask: See this [installation guide](https://flask.palletsprojects.com/en/1.1.x/installation/#installation).
   - OpenAI API: See this [quickstart guide](https://platform.openai.com/docs/quickstart).
   - Google API: See this [quickstart guide](https://developers.google.com/drive/api/quickstart/python).

# Usage
Run app.py with python:
```
pyhon app.py
```

This is to be used in a similar way to other GPT-based assistants but can handle simple questions about a user's schedule as well. getCalander.py can be tweaked to include more events if needed. 

# Known Issues/Constraints
 - Markdown code blocks and formatting not supported
 - User can send messages before AI has responded
 - AI may "break character" after a few outputs due to current token managing code

# Planned Features/Fixes
 - Support for code formatting
 - Restrict user input while AI generates response
 - Improve token management
 - Include context specifc information triggers (i.e the word calendar sends calendar information to AI)

# Acknowledgements
 - [OpenAI Example Code](https://platform.openai.com/examples)
 - [Google Calander API Guide](https://developers.google.com/calendar/api/guides/overview)
 - [Flask Quickstart Guide](https://flask.palletsprojects.com/en/2.3.x/quickstart/)

# Build a GPT3 Chatbot for your Company

_Build your own AI virtual assistant using your company documentation and GPT3_

# Set Up

1. Get your OpenAI API key and add it **Secrets** as `OPENAI_API_KEY`
2. Make up and `API_KEY` for the JSON API, this can just be something like a password if you'd like
3. Fill the `training/facts` folder with as many `text` documents as you can containing information about the company you're training it on. Top tips would be handbooks, websites, how-to guides, and anything public facing.
4. Please don't put anything top secret in there, no one wants their company financials leaked by an AI chatbot!
5. Edit the `master.txt` file to represent how you want the bot to behave when interacting with the users
6. Click **Run**, select option `1`
7. To chat with the bot, once you've one the training, select option `2`

## JSON API (Advanced Users)
Option 3, or stating automatically after five seconds on the menu, is the JSON API. You can use POST requests to this Repl's `repl.co` address to take the chat to a different location or app.

Here's a quick guide to dealing with the API part in Python

`import requests`

### data to be sent to the server
`data = {'key': 'YOUR API KEY', 'question': 'Your question', 'history': 'previous questioning history'}`

### sending post request and saving response as response object 
`r = requests.post(url = URL, data = data) `
  
### extracting response json 
`response_data = r.json() `
  
### printing response 
`print(response_data)`

# Credit

All based on the [Amjad Masad Chat bot](https://ai.repl.page) by IronCladDev on Replit
For more information on how this works, check out [Zahid Khawaja's Tutorial](https://replit.com/@zahidkhawaja/Replit-Assistant?v=1).

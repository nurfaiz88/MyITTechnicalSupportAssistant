# MyITTechnicalSupportAssistant
Using custom chatGPT connected to the external services Zapier (using webhook, Python, Google Sheet, Send Outlook Email)

STEP 1: Custom ChatGPT Configuration
1. Go to "https://chatgpt.com/gpts" > click create.
2. Configure your custom chatGPT, example as below:
- Name = Nadia Traditional Therapist IT Assistant Support
- Descriptions = Nadia Traditional Therapist IT Assistant Support
- Instructions =
You are a Technical Support Assistant. 
Your job is to collect the required information from the user:
1. Please specify your name (e.g: Faiz)
2. Please specify your Email Address (e.g: test@nadiatraditionaltherapist.org)
3. Please specify issue that you are facing (e.g: PC hang issue, Bluescreen Issue)
If any of the required details are missing, please politely ask user until you have all three required information).
Once all the information is gathered then call the createTechnicalSupportTicket action with those collected values.
- Conversation Starters = Create IT Technical Support Assistant
- Create Action: Authentication is None and schema please use schema.json. You need to add your endpoint URL. To get you Zapier endpoint URL. Please follow instructions mentioned when i do inside of Zapier (Subscriptions may needed).
  3. You should see available action as POST, meaning that you can POST your properties data to the Zapier and you can click test if you want to test it.
  4. Save your custom ChatGPT.

  STEP 2: Zapier Configuration
  

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
1. Please specify your name (e.g: UserName)
2. Please specify your Email Address (e.g: tUserEmailAddress)
3. Please specify issue that you are facing (e.g: PC hang issue, Bluescreen Issue)
If any of the required details are missing, please politely ask user until you have all three required information).
Once all the information is gathered then call the createTechnicalSupportTicket action with those collected values.
- Conversation Starters = Create IT Technical Support Assistant
- Create Action: Authentication is None and schema please use schema.json. You need to add your endpoint URL. To get you Zapier endpoint URL. Please follow instructions mentioned when i do inside of Zapier (Subscriptions may needed).
3. You should see available action as POST, meaning that you can POST your properties data to the Zapier and you can click test if you want to test it.
4. Save your custom ChatGPT.

STEP 2: Zapier Configuration
1. Go to this link https://zapier.com/
2. Please subscribe at least Zapier Pro Plan (Individual), around USD29. This is required since we need to use the Zapier Webhook (require premium account)
3. Go to Zapier Home https://zapier.com/app/home > click create.
4. Choose App Webhook by Zapier with trigger event as catch hook > Click Continue > On Configure, click continue > On Test, wait here. you need to perform validation. Open terminal and run this command curl -X POST <<COPY_YOUR_WEBHOOK_URL_AND_PASTE_HERE>> -H "Content-Type: application/json" -d '{"name":USERNAME","email":"USEREMAIL","issueDescription":"PC Hang"}' > Once validation done no issue then come back to the Test page, click find new records. You should see new records/properties that you pass from validation process including name, email, issueDescription > Click continue with the selected records.
5. Next App creation is code by zapier with action event run python and click continue > On configure write the code as mentioned in GenerateITTicketNumber.py

Overall Zapier workflow:
<img width="2788" height="1818" alt="image" src="https://github.com/user-attachments/assets/20c4c8df-5906-4ac9-a1ca-d3c1de597364" />


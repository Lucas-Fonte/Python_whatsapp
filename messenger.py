import os
from twilio.rest import Client 
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN') 
messageContent = os.getenv('MESSAGE_CONTENT')
mediaUrl = os.getenv('MEDIA_URL')

contactNumbers = {
    "from": os.getenv('NUMBER_FROM'),
    "to": os.getenv('NUMBER_TO')
}

client = Client(account_sid, auth_token) 

message = client.messages.create( 
                              from_= contactNumbers["from"],  
                              to= contactNumbers["to"],
                              body=messageContent, 
                              media_url=[mediaUrl]     
                          ) 
 
print('Message sent succesfully! \nMessage id: ' + message.sid)








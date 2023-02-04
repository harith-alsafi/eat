import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv

load_dotenv()

sg = sendgrid.SendGridAPIClient(api_key=os.getenv('SENDGRID_API_KEY'))
from_email = Email("swaronacharjee@gmail.com")  # Change to your verified sender
to_email = To("harith.alsafi@gmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)

# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
# from dotenv import load_dotenv

# load_dotenv()

# message = Mail(
#     from_email='swaronacharjee@gmail.com',
#     to_emails='swaronacharjee@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')

# sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
# response = sg.send(message)
# print(response.status_code, response.body, response.headers)
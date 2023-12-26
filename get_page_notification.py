import requests
import smtplib
import ssl

from email.message import EmailMessage

url = "https://watershed.com/careers/4096445004-software-engineer-intern"
response = requests.head(url)

sender_email = 'NotifEyeSender@gmail.com'
email_access = 'ywcy udtd tedo bblv'
recipient_email = 'hassan.alawie10@gmail.com'



if response.status_code == 200:
    subject = 'APPLY FOR WATERSHED'
    body = """
    GO APPLY OVER HERE https://watershed.com/careers/4096445004-software-engineer-intern
    """
    em = EmailMessage()
    em['From'] = sender_email
    em['To'] = recipient_email
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, email_access)
        smtp.sendmail(sender_email, recipient_email, em.as_string())
else:
    print("URL Not up yet")

import smtplib
from email.message import EmailMessage
import os

def send_mail(sender, app_password, receiver, subject, body):
    try:
        # Step 1: Create Email object
        msg = EmailMessage()

        # Step 2: Set mail headers
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        # Step 3: Set mail body
        msg.set_content(body)

        # Step 4: Create SMTP SSL connection
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        # Step 5: Login using Gmail + App password
        smtp.login(sender, app_password)

        # Step 6: Send the email
        smtp.send_message(msg)

        # Step 7: Close the connection
        smtp.quit()
        return True, None

    except Exception as e:
        return False, str(e)
    
    
def send_mail_with_attachment(sender, app_password, receiver, subject, body, attachment_file_path):
    try:
        msg = EmailMessage()

        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        msg.set_content(body)

        # Add the attachment
        if attachment_file_path and os.path.exists(attachment_file_path):

            with open(attachment_file_path, 'rb') as fobj:
                file_content = fobj.read()
                file_name = os.path.basename(attachment_file_path)
            msg.add_attachment(file_content, maintype='application', subtype='octet-stream', filename=file_name)

        else:
            # If attachment path is invalid, log it but don't fail the email sending
            return False, f"Warning: Attachment file not found or path invalid: {attachment_file_path}"

        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

        smtp.login(sender, app_password)

        smtp.send_message(msg)

        smtp.quit()
        return True, None

    except Exception as e:
        return False, str(e)
    

def main():
    sender_email = "demo.shan24@gmail.com"
    app_password = "rjkgsuuhrlvqesmi"
    reciever_mail = "cpshantanu5@gmail.com" 

    subject = "Test Mail from Python Script"

    body = """ Jay Ganesh, 
    This is a test email sent using Marvellous Python. 

    Regards,
    Marvellous Infosystems
    """

    Ret = send_mail(sender_email, app_password, reciever_mail, subject, body)
    if Ret == True:
        print("Mail sent successfully")
    else:
        print("Error: Unable to send mail")


if __name__ == "__main__":
    main()

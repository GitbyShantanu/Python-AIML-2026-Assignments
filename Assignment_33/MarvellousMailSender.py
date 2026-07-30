import smtplib
from email.message import EmailMessage
import os

def send_mail(sender, app_password, receiver, subject, body):
    """Sends a simple email without attachments."""

    # Create email message object.
    msg = EmailMessage()
    # Set email headers.
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    # Set email body.
    msg.set_content(body)

    # Connect to Gmail's SMTP server and send the email.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
    
    
def send_mail_with_attachment(sender, app_password, receiver, subject, body, attachment_file_path):
    """
    Sends an email with an attachment.
    This function will raise exceptions on failure (e.g., login error, file not found),
    which are intended to be caught by the calling function in FileUtils.py.
    """
    # Create email message object.
    msg = EmailMessage()
    # Set email headers.
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    # Set email body.
    msg.set_content(body)

    # Add the attachment if the path is valid.
    if attachment_file_path and os.path.exists(attachment_file_path):
        # Read attachment file in binary mode.
        with open(attachment_file_path, 'rb') as fobj:
            file_content = fobj.read()
            file_name = os.path.basename(attachment_file_path)
        # Add the attachment, specifying the maintype and subtype for plain text.
        msg.add_attachment(file_content, maintype='text', subtype='plain', filename=file_name)
    else:
        raise FileNotFoundError(f"Attachment file not found or path invalid: {attachment_file_path}")

    # Connect to Gmail's SMTP server, login, and send the email.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, app_password)
        smtp.send_message(msg)
    

def main():
    # --- Test Data ---
    sender_email = "demo.shan24@gmail.com"
    app_password = "rjkgsuuhrlvqesmi"
    reciever_mail = "cpshantanu5@gmail.com" 

    subject = "Test Mail from Python Script"

    body = """ Jay Ganesh, 
    This is a test email sent using Marvellous Python. 

    Regards,
    Marvellous Infosystems
    """

    # This main function is for testing the module directly.
    try:
        print("Attempting to send a test email...")
        # To test the attachment function, you would call send_mail_with_attachment here.
        send_mail(sender_email, app_password, reciever_mail, subject, body)
        print("Test mail sent successfully!")
    except Exception as e:
        print(f"Error sending test mail: {e}")

if __name__ == "__main__":
    main()

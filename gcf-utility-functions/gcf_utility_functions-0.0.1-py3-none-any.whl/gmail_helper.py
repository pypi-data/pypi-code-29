
import os
import sys
import base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from apiclient import errors
from gcf_utility_functions import google_service_access

def add_attachment(file, message):
    try:
        with open(file, 'rb') as fp:
            msg = MIMEBase('application', "octet-stream")
            msg.set_payload(fp.read())
        encoders.encode_base64(msg)
        msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
        message.attach(msg)
    except IOError:
        print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
        raise


def create_message(sender, to, subject, message_text, file=None, cc=None):
    """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver. For multiple recipients, include as list.
    subject: The subject of the email message.
    message_text: The text of the email message.
    file (optional): The path to the file(s) to be attached. For multiple files, include as list.
    cc (optional): Email address of additional recipients. For multiple cc recipients, include as list.

  Returns:
    An object containing a base64url encoded email object.
  """

    message = MIMEMultipart()
    msg = MIMEText(message_text, 'html')
    message.attach(msg)
    message['from'] = sender
    message['subject'] = subject

    if type(to) is list:
        message['to'] = ", ".join(to)
    else:
        message['to'] = to

    if cc:
        if type(cc) is list:
            message['cc'] = ", ".join(cc)
        else:
            message['cc'] = cc

    if type(file) is list:
        for item in file:
            add_attachment(item, message)
    elif file:
        add_attachment(file, message)
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    return {'raw': raw}


def create_draft(message_body):
    """Create and insert a draft email. Print the returned draft's message and id.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message_body: The body of the email message, including headers.

  Returns:
    Draft object, including draft id and message meta data.
  """
    try:
        service = google_service_access.build_service_object('gmail')
        message = {'message': message_body}
        draft = service.users().drafts().create(userId='me', body=message).execute()
        print('SUCCESS: ' + draft['id'], draft['message'])

    except errors.HttpError as error:
        print('An error occurred: {}'.format(error))


def send_message(message):
    """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
    try:
        service = google_service_access.build_service_object('gmail')
        message = (service.users().messages().send(userId='me', body=message)
                   .execute())
        print('SUCCESS: ' + message['id'])

    except errors.HttpError as error:
        print('An error occurred: {}'.format(error))

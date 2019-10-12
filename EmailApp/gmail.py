from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes

SCOPES = ['https://mail.google.com/','https://www.googleapis.com/auth/gmail.readonly']

basedir = os.path.abspath(os.path.dirname(__file__))
data_json = basedir +'/credentials.json'


class MailManager:
    def __init__(self):
        self.creds = None
        self.service = None
        self.managecredentials()

    def managecredentials(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(data_json, SCOPES)
                self.creds = flow.run_local_server(host='127.0.0.1',port=8000)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)
        self.service = build('gmail', 'v1', credentials=self.creds)

    def ListMessagesMatchingQuery(self, user_id, query=''):
        try:
            response = self.service.users().messages().list(userId=user_id,q=query).execute()
            messages = []
            if 'messages' in response:
                messages.extend(response['messages'])
            while 'nextPageToken' in response:
                page_token = response['nextPageToken']
                response = self.service.users().messages().list(userId=user_id, q=query,pageToken=page_token).execute()
                messages.extend(response['messages'])
            return messages
        except:
            print('An error occurred: ')

    def CreateMessage(self,sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
        b64_string = b64_bytes.decode('utf-8')
        return {'raw': b64_string}

    def CreateMessageWithAttachment(self, sender, to, subject, message_text, file_dir,filename):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

        msg = MIMEText(message_text)
        message.attach(msg)
        path = os.path.join(file_dir + '/EmailApp/attachments/', filename)
        content_type, encoding = mimetypes.guess_type(path)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)

        fp = open(path, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()

        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)
        b64_bytes = base64.urlsafe_b64encode(message.as_bytes())
        b64_string = b64_bytes.decode('utf-8')
        return {'raw': b64_string}


if __name__ == '__main__':
    obj = MailManager()
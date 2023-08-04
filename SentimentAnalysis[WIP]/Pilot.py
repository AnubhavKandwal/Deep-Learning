from __future__ import print_function
from os import name
import pickle
import os.path
import io
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

#defining scope to control the files in google drive
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def main():
    creds = drive_handle()
    service = build('drive', 'v3', credentials=creds)
    print('Enter name of file with extension: ',end=' ')
    name = input()
    #create_file(service, name)
    filelist = file_list(service)
    print(filelist)
    #print('Do you wish to download a file: ',end=' ')
    #option = input()
    #print(option)
    #if option == 'yes':
    #    print('Enter name of file with extension: ',end=' ')
    #    file = input()
    #    download_file(service, file)
    #else:
    #    print('thanks')

def drive_handle():
    #to generate token for access to google drive

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def create_file(service, filename):
    filemetadata = {
        'name': '{0}'.format(filename)
    }
    filecreate = service.files().create(body=filemetadata).execute()
    print('File is created of name: {0} and ID: {1}'.format(filename, filecreate['id']))

def get_doc_id(service ,name):
    items = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
    print(items)
    id = None
    for i in items['files']:
        if i['name'] == name:
            id = i['id']
    return id

def download_file(service, name):
    Id = get_doc_id(service,name)
    request = service.files().get_media(fileId=Id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))

def file_list(service):
    results = service.files().list(q="name contains 'WhatsApp'", spaces='drive', fields='nextPageToken, files(id, name)').execute()
    items = results.get('files', [])
    return items

if __name__ == '__main__':
    main()
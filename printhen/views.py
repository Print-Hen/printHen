
from django.http import HttpResponse
import json
import betterimap
import requests
import httplib2

from apiclient import discovery
from oauth2client import client
from django.shortcuts import redirect


def index(request):
    if 'credentials' not in request.session:
        return redirect('oauth2callback')
    credentials = client.OAuth2Credentials.from_json(request.session['credentials'])
    if credentials.access_token_expired:
        return redirect('oauth2callback')
    else:
        http_auth = credentials.authorize(httplib2.Http())
        gmail_service = discovery.build('gmail', 'v1', http_auth)
        results = gmail_service.users().labels().list(userId='me').execute()
        labels = results.get('labels',[])
        if not labels:
            print('No labels found.')
        else:
            print('Labels:')
            for label in labels:
                print(label['name'])


def oauth2callback(request):
    flow = client.flow_from_clientsecrets(
        'client_secrets.json',
        scope='https://www.googleapis.com/auth/gmail.readonly',
        redirect_uri='http://192.168.43.69.xip.io:8000/')
    print request.POST.get('code','HELLO');
    if request.POST.get('code',None) is None:
        auth_uri = flow.step1_get_authorize_url()
        return redirect(auth_uri)
    else:
        auth_code = request.POST.get('code','')
        credentials = flow.step2_exchange(auth_code)
        request.session['credentials'] = credentials.to_json()
        return redirect('index')



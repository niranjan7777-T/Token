import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
client_id = 'your_client_id_here'
client_secret = 'your_client_secret_here'
token_url = 'https://example.com/oauth2/token'
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)
token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
print(token['access_token'])

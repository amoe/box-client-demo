import json
import boxsdk
import boxclientdemo.http_server
import urllib.parse

# sussex/boxdownloader credentials

with open('credentials.json', 'r') as f:
    credentials = json.load(f)


#REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'  # unsupported
# FIXME: Find an unused port
REDIRECT_URI = 'http://localhost:49152/'

def my_store_tokens(access_token, refresh_token):
    print("My code: access token:", access_token)
    print("My code: refresh token:", refresh_token)

oauth = boxsdk.OAuth2(
    client_id=credentials['client_id'],
    client_secret=credentials['client_secret'],
    store_tokens=my_store_tokens
)

auth_url, csrf_token = oauth.get_authorization_url(REDIRECT_URI)

print(auth_url)
print(csrf_token)

last_path = boxclientdemo.http_server.run()

val = urllib.parse.urlparse(last_path)
q = urllib.parse.parse_qs(val.query, strict_parsing=True, errors='strict')

the_csrf = q['state'][0]
the_code = q['code'][0]




assert the_csrf == csrf_token

# Control jumps to my_store_tokens after here
access_token, refresh_token = oauth.authenticate(the_code)

client = boxsdk.Client(oauth)

print("Resuming")
user = client.user().get()
print('The current user ID is {0}'.format(user.id))

TEST_FOLDER_ID = '104799745798'

folder = client.folder(folder_id=TEST_FOLDER_ID).get()
print('Folder "{0}" has {1} items in it'.format(
    folder.name,
    folder.item_collection['total_count'],
))

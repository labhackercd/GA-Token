# service-account.py

from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import HttpAccessTokenRefreshError

# The scope for the OAuth2 request.
SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

# The location of the key file with the key data.
KEY_EDEMOCRACIA = 'json-key-edemocracia.json'
KEY_ENQUETES = 'json-key-enquetes.json'


# Defines a method to get an access token from the ServiceAccount object.
def get_access_token(account: str) -> str:
    if account == 'edemocracia':
        KEY_FILEPATH = KEY_EDEMOCRACIA
    elif account == 'enquetes':
        KEY_FILEPATH = KEY_ENQUETES
    else:
        KEY_FILEPATH = ''

    try:
        token = ServiceAccountCredentials.from_json_keyfile_name(
            KEY_FILEPATH, SCOPE).get_access_token().access_token
    except HttpAccessTokenRefreshError:
        token = 'Account not have permission'
    except Exception:
        token = 'Error token'
    
    return token

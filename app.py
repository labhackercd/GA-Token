from flask import Flask
from service_account import get_access_token
app = Flask(__name__)


@app.route('/')
def hello_world():
    token = get_access_token()
    return {"token": token}, 200

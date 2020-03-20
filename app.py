from flask import Flask
from service_account import get_access_token
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    token = get_access_token()
    return {"token": token}, 200

if __name__ == '__main__':
    app.run()

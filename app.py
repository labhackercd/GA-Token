from flask import Flask
from service_account import get_access_token
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/edemocracia')
def token_edemocracia():
    token = get_access_token('edemocracia')
    return {"token": token}, 200


@app.route('/enquetes')
def token_enquetes():
    token = get_access_token('enquetes')
    return {"token": token}, 200


if __name__ == '__main__':
    app.run()

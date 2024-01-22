from flask import Flask, jsonify
from flask_cors import CORS
import requests

api_key = "RGAPI-e6017d87-7dd7-45ba-b85e-213a2896be68"
api_url_summoner = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Dom%20Noway"

api_url = api_url_summoner +'?api_key=' + api_key

response_object = requests.get(api_url)

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return (response_object.json())


if __name__ == '__main__':
    app.run()
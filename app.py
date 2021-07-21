from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_chuck_norris_jokes():

    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url).json()

    return  response

@app.route('/category',methods=['GET','POST'])
def get_chuck_image():
    api_url = 'https://api.chucknorris.io/jokes/categories'
    response = requests.get(api_url).json()

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

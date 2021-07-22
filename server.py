from flask import Flask, render_template
import requests
import random
import datetime
app = Flask(__name__)

AGIFYAPI = "https://api.agify.io?name="
GENDERIZEAPI= "https://api.genderize.io?name="



@app.route('/guess/<guessname>')
def guess(guessname):
    agify_response = requests.get(AGIFYAPI+guessname)
    agify_response.raise_for_status()
    raw_data = agify_response.json()
    genderize_response = requests.get(GENDERIZEAPI+guessname)
    genderize_response.raise_for_status()
    gender_data = genderize_response.json()
    return render_template('index.html', your_name=raw_data["name"].capitalize(), age=raw_data["age"], gender=gender_data["gender"])


if __name__=="__main__":
    app.run(debug=True)


from flask import Flask, render_template, request
from pymongo import MongoClient
import pandas as pd
import pickle

app = Flask(__name__)
db_client = MongoClient('localhost', 27017)

# data = db_client.details
# storage = data.storage
#andorid_model = pickle.load(open("../exploratory-analysis/android_model.pkl", "rb"))
#apple_model = pickle.load(open("../exploratory-analysis/apple_model.pkl", "rb"))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        os = request.form.get('os')
        front_camera = request.form.get('front_camera')
        ram = request.form.get('ram')
        battery = request.form.get('battery')
        storage = request.form.get('storage')
        score = request.form.get('score')
        scree_size = request.form.get('screen_size')
        refresh_rate = request.form.get('refresh_rate')
        main_camera = request.form.get('main_camera')

        new_inputs = []
        num_camera = len(request.form)
        for i in range(2, num_camera):
            new_input = request.form.get(f'new-input-{i}')
            if new_input is not None:
                new_inputs.append(new_input)

        s = pd.Series([])

        print(f'OS: {os}, Front camera: {front_camera}, Ram: {ram}, Battery: {battery}, Storage: {storage}, Score: {score}, Screen size: {scree_size}, Refresh rate: {refresh_rate}, Main camera: {main_camera}, New Inputs: {new_inputs}')
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

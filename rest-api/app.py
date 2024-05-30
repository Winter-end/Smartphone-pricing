from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
db_client = MongoClient('localhost', 27017)

# data = db_client.details
# storage = data.storage

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        os = request.form.get('os')
        ram = request.form.get('ram')
        battery = request.form.get('battery')
        storage = request.form.get('storage')
        # You can now use the form data
        print(f'OS: {os}, Ram: {ram}, Battery: {battery}, Storage: {storage}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'index-test'
    
@app.route('/tac_status')
def tac_status():
    return 'sharmapriyanka2585@gmail.com'

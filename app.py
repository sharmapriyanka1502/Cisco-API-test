from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "sharmapriyanka2585@gmail.com"
    
@app.route("/tac_status")
def tac_status():
    return "sharmapriyanka2585@gmail.com"
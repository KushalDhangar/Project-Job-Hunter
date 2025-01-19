from flask import Flask # Flask is class and flask is a module
# Flask Web Server Created
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "hello ,Kushal"

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
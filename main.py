from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/h")
def getHello():
    return jsonify({"hello":"world"})

@app.errorhandler(404)
@app.route('/<lol>')
def not_found(lol):
    return "<h1>Oops, I guess You are Lost?</h1>"

if __name__ == '__main__':
    app.run(debug=True)

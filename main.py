from flask import Flask
from src.routes import traders, investments, general

app = Flask(__name__)

app.register_blueprint(traders)
app.register_blueprint(investments)
app.register_blueprint(general)
app.secret_key = "hola"


@app.errorhandler(404)
def method_not_allowed(a):
    return "not found pls ask for help"


@app.errorhandler(404)
def not_found(a):
    return "not found pls ask for help"


@app.errorhandler(401)
def forbiden(a):
    return "forbiden"


@app.errorhandler(400)
def bad_request(a):
    return "not found pls ask for help"


@app.errorhandler(500)
def server_error(a):
    return "woops something wrong"


if __name__ == "__main__":
    app.run(debug=True)

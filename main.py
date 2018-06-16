from flask import Flask

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return "Hello from Flask"

if __name__ == "__main__":
    myapp.run(debug=True)

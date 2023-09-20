from flask import Flask
from flask_migrate import Migrate
# from models import 

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to jambodada"






if __name__ == '__main__':
    app.run(debug=True)
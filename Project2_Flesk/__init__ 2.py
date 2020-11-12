from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cop481333'

from Project2_Flesk import routes

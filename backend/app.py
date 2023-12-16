from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import *
from database import Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{serverUser}:{serverPassword}@{serverHost}:{serverPort}/{serverDatabase}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
    
@app.route('/')
def firstPage():
    return 'Hello from flask!'

@app.route('/home')
def home():
    return 'Welcome Home'

if __name__ == '__main__':
    app.run(debug=True)
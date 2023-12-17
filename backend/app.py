from datetime import timedelta

from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_cors import CORS
from flask import Flask, request, jsonify, session
from utils import *
from database import db, Users

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{serverUser}:{serverPassword}@{serverHost}:{serverPort}/{serverDatabase}'
app.secret_key = flaskAppSecretKey
app.config['SESSION_FILE_THRESHOLD'] = 100 
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=5)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

db.init_app(app)
server_session = Session(app)
bcrypt = Bcrypt(app)

with app.app_context() as ctx:
    db.create_all()
    
@app.route("/api/login", methods=["POST"])
def login_user():
    login = request.json["login"]
    password = request.json["password"]
 
    user = Users.query.filter_by(login=login).first()
 
    if user is None:
        return jsonify({"error": "Unauthorized Access"}), 401
 
    if not bcrypt.check_password_hash(user.password_hash, password):
        return jsonify({"error": "Unauthorized"}), 401
    
    session["user_id"] = user.id

    return jsonify({
        "session_id": session["user_id"]
    })
    
@app.route("/api/create_user", methods=["POST"])
def create_user():
    login = request.json["login"]
    password = request.json["password"]
    isSuper = request.json["is_super"]
    id = request.json["id"]
    departamentId = request.json["departament_id"]
    email = request.json["email"]
    adminLogin = request.json["adminLogin"]
    adminPassword = request.json["adminPassword"]
    
    if adminLogin != flaskAppAdminLogin or adminPassword != flaskAppAdminPassword:
        return jsonify({"error": "Unathorized access"}), 410
    
    userExists = Users.query.filter_by(login=login).first() is not None
    
    if userExists:
        return jsonify({"error": "User already exists"}), 409
    
    hashedPassword = bcrypt.generate_password_hash(password).decode('utf-8')

    newUser = Users(login = login, password_hash = hashedPassword, id = id, is_super = isSuper, departament_id = departamentId, email = email, session_key = None)
    db.session.add(newUser)
    db.session.commit()
    
    return

@app.route("/api/get_employees")
def getEmployee():
    userId = session.get("user_id")
 
    if not userId:
        return jsonify({"error": "Unauthorized Access"}), 401
     
    user = Users.query.filter_by(id=userId).first()
    return jsonify({
        "id": user.id,
        "email": user.email
    })
    
if __name__ == '__main__':
    app.run(host=flaskAppHost, port=flaskAppPort, debug=flaskAppDebugMode)
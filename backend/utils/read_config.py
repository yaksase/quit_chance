import configparser

configObj = configparser.ConfigParser()
configObj.read('backend/config.ini')

serverParameters = configObj['postgresql']
serverUser = serverParameters['user']
serverPassword = serverParameters['password']
serverHost = serverParameters['host']
serverPort = serverParameters['port']
serverDatabase = serverParameters['database']

flaskAppParameters = configObj['flask_app']
flaskAppHost = flaskAppParameters['host']
flaskAppPort = flaskAppParameters['port']
flaskAppDebugMode = bool(flaskAppParameters['debug'])
flaskAppAdminLogin = flaskAppParameters['admin_login']
flaskAppAdminPassword = flaskAppParameters['admin_password']
flaskAppSecretKey = flaskAppParameters['secret_key']
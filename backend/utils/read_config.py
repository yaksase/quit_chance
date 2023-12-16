import configparser

configObj = configparser.ConfigParser()
configObj.read('backend/config.ini')
serverParameters = configObj['postgresql']

serverUser = serverParameters['user']
serverPassword = serverParameters['password']
serverHost = serverParameters['host']
serverPort = serverParameters['port']
serverDatabase = serverParameters['database']
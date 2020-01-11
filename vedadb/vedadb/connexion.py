import os
import simplejson
from pg import DB
from sqlalchemy import create_engine
# parameters_path = sys.argv[1]
# def connect():
#     with open(parameters_path, 'r') as fich_p:
#         parameters = simplejson.loads(fich_p.read())
        

def connect(parameters_path):
    with open(parameters_path, 'r') as fich_p:
        parameters = simplejson.loads(fich_p.read())
        db = DB(dbname=parameters['dbname'], host=parameters['dbserver'], 
        port=parameters['dbport'],user=parameters['dbuser'], passwd=parameters['dbpass'])
        return db

def connectEngine(parameters_path):
    with open(parameters_path, 'r') as fich_p:
        parameters = simplejson.loads(fich_p.read())
        # username:password@host:port/database
        engine = create_engine('postgresql://'+
        str(parameters['dbuser'])+':'+
        str(parameters['dbpass'])+'@'+
        str(parameters['dbserver'])+':'+
        str(parameters['dbport'])+'/'+
        str(parameters['dbname']))
        return engine
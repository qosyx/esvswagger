__all__ = ['set']
import threading
import sys
import os
import re
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import vedadb.connexion as connexion
import vedadb.entete as entete

    
def readVdeToSetTable(myfile):
    typedimensionset=[]
    region=[]
    codeset=[]
    periode=[]
    description=[]

    with open(myfile) as f:
        for line in f:
            if(re.findall(r'[A-Z,a-z]+SET', line)!=[]):
                line=line.split(",")
                typedimensionset.append(line[0].split('"')[1].strip())
                region.append(line[1].split('"')[1].strip())
                codeset.append(line[2].split('"')[1].strip())
                description.append(line[3].split('"')[1].strip())
        df = pd.DataFrame({'typedimensionset':typedimensionset,
        'region':region,'codeset':codeset,'description':description})
    return df

def setToDb(parameters_path,db,line=[],importid=""):
        line['importid'] = importid
        engine=connexion.connectEngine(parameters_path)
        line.to_sql(name='set', con=engine, if_exists = 'append', index=False)

                
def readSetIdFromDb(db,importID=0):
        result = {}
        for r in db.query(  # just for example
                "SELECT * FROM set WHERE importid=importID"
                ).dictresult():
                result.update({r['codeset']:r['idset'] })
        return result
                # print(r['idset'])

def executionInExitingDb(parameters_path,myvdefile,importId):
    db=connexion.connect(parameters_path)
    line=readVdeToSetTable(myvdefile)
    setToDb(parameters_path,db,line,importId)

def execution(parameters_path,myvdefile):
    db=connexion.connect(parameters_path)
    importId=entete.readImportIdFromDb(db)
    line=readVdeToSetTable(myvdefile)
    setToDb(parameters_path,db,line,importId)

if __name__ == '__main__':
    parameters_path = sys.argv[1]
    myvdefile = sys.argv[2]
    db=connexion.connect(parameters_path)
    importId=entete.readImportIdFromDb(db)
    db=connexion.connect(parameters_path)
    line=readVdeToSetTable(myvdefile)
    setToDb(parameters_path,db,line,importId)


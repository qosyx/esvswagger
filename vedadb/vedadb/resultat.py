__all__ = ['resultat']
import sys
import os
import re
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import vedadb.connexion as connexion
import vedadb.fileToDataframe as file
import vedadb.entete as entete
from pgdb import connect
from sqlalchemy import create_engine

def readVdeToSetTable(myfile):
    d = {}
    attribut=[]
    commodity=[]
    process=[]
    periode=[]
    region=[]
    vintage=[]
    timeslice=[]
    userconstraint=[]
    pv=[]
    with open(myfile) as f:
        result={}
        for line in f:
            if not(re.findall(r'^\*', line)!=[]):
                # print(line)
                
                if(line==""):
                    pass
                else:
                    try:
                        line=line.split(",")
                        attribut.append(line[0].split('"')[1].strip())
                        commodity.append(line[1].split('"')[1].strip())
                        process.append(line[2].split('"')[1].strip())
                        periode.append(line[3].split('"')[1].strip())
                        region.append(line[4].split('"')[1].strip())
                        vintage.append(line[5].split('"')[1].strip())
                        timeslice.append(line[6].split('"')[1].strip())
                        userconstraint.append(line[7].split('"')[1].strip())
                        pv.append(line[8].split("\n")[0])
                        
                    except IndexError:
                        pass
        df = pd.DataFrame({'attribut':attribut,
        'commodity':commodity,'process':process,'periode':periode,'region':region,'vintage':vintage,
        'timeslice':timeslice,'userconstraint':userconstraint,'pv':pv})
    return df

def writeResultInDb(parameters_path,db,line,importid=1):
        line['importid'] = importid
        engine=connexion.connectEngine(parameters_path)
        line.to_sql(name='resultat', con=engine, if_exists = 'append', index=False)


def execution(parameters_path,myvdfile):
    db=connexion.connect(parameters_path)
    df=readVdeToSetTable(myvdfile)
    importId=entete.readImportIdFromDb(db)
    writeResultInDb(parameters_path,db,df,importId)

def executionInExitingDb(parameters_path,myvdfile,importId):
    db=connexion.connect(parameters_path)
    df=readVdeToSetTable(myvdfile)
    writeResultInDb(parameters_path,db,df,importId)

if __name__ == "__main__":
    parameters_path = sys.argv[1]
    myvdfile = sys.argv[2]
    db=connexion.connect(parameters_path)
    df=readVdeToSetTable(myvdfile)
    importId=entete.readImportIdFromDb(db)
    writeResultInDb(parameters_path,db,df,importId)
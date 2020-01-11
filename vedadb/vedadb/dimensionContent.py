__all__ = ['dimensioncontent']
import time 
import sys
import os
import re
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import vedadb.connexion as connexion
import vedadb.adress as ping
import vedadb.entete as entete
import vedadb.fileToDataframe as file
import vedadb.sets as set
from pgdb import connect
from sqlalchemy import create_engine

#Attention les attributs ont belle et bien codedimension, mais n'ont pas codeSet

def attributToSave(vdedf):
    # vdedf.filter(items=['dimension'],like)
    attribut=vdedf[vdedf['dimension'] == 'Attribute']
    attribut=attribut.rename(columns={"dimension": "typedimension", "region": "region","codset":"codeset","description":"descriptiondimensioncode"})
    return attribut


def otherDimensionContentValue(vdsdf,vdedf):
    result = {}
    resultvds=vdsdf.drop_duplicates(subset='dimensionCode', keep="last") 
    vdedf=vdedf.drop_duplicates(subset='codset', keep="last") 
    resultvds=resultvds[resultvds['dimension']!='Attribute']
    for index, row in resultvds.iterrows():
        search = row.to_dict()['dimensionCode']
        for index,row in vdedf.iterrows():
            if(search==row.to_dict()['codset']):
                result.update({search: row.to_dict()['description']})
    return result

def updateVdsDataframe(vdsdf,resultOfVdsVde):
    dimension=[]
    region=[]
    codset=[]
    dimensionCode=[]
    description=[]
    for index, row in vdsdf.iterrows():
        for key,value in resultOfVdsVde.items():
            if(row.to_dict()['dimensionCode']==key):
                dimension.append(row.to_dict()['dimension'])
                region.append(row.to_dict()['region'])
                codset.append(row.to_dict()['codset'])
                dimensionCode.append(row.to_dict()['dimensionCode'])
                description.append(value)
    df = pd.DataFrame({'typedimension':dimension,
        'region':region,'codeset':codset,'dimensionCode':dimensionCode,'descriptiondimensioncode':description})
    return df


#En fait je veux à partir des id des sets update aux dimensions code
#C'est le rôle de cette fonction
def dimensionContentToSave(result,idtable):
    dimension=[]
    region=[]
    codset=[]
    dimensionCode=[]
    description=[]
    setid=[]
    for index, row in result.iterrows():
        p=0
        for key,value in idtable.items():
            if (row.to_dict()['codeset']==key):
                p=1
                dimension.append(row.to_dict()['typedimension'])
                region.append(row.to_dict()['region'])
                codset.append(row.to_dict()['codeset'])
                dimensionCode.append(row.to_dict()['dimensionCode'])
                description.append(row.to_dict()['descriptiondimensioncode'])
                setid.append(value)
        if p==0:
                value=""
                dimension.append(row.to_dict()['typedimension'])
                region.append(row.to_dict()['region'])
                codset.append(row.to_dict()['codeset'])
                dimensionCode.append(row.to_dict()['dimensionCode'])
                description.append(row.to_dict()['descriptiondimensioncode'])
                setid.append(value)
    df = pd.DataFrame({'typedimension':dimension,
        'region':region,'codeset':codset,'idset':setid,'dimensioncode':dimensionCode,'descriptiondimensioncode':description})
    return df


def writeDimensionContentInDb(parameters_path,db,line,importid=1):
    
        line['importid'] = importid
        engine=connexion.connectEngine(parameters_path)
        line.to_sql(name='dimensioncontent', con=engine, if_exists = 'append', index=False)


def writeAttributDimensionContentInDb(parameters_path,db,line,importid=1):
        
        line['importid'] = importid
        engine=connexion.connectEngine(parameters_path)
        line.to_sql(name='dimensioncontent', con=engine, if_exists = 'append', index=False)

       



def execution(parameters_path,myfile,mysfile):
    db=connexion.connect(parameters_path)
    vdedf=file.vdeToDataframe(myfile)
    vdsdf=file.vdsToDataframe(mysfile)
    result=otherDimensionContentValue(vdsdf,vdedf)
    d=updateVdsDataframe(vdsdf,result)
    importId=entete.readImportIdFromDb(db)

    idtable=set.readSetIdFromDb(db,importId)
    d=dimensionContentToSave(d,idtable)

    # #enregistrement de contentDimension sauf les attributs
    writeDimensionContentInDb(parameters_path,db,d,importId)
    

    # #Enregistrement des dimensions attributs
    writeAttributDimensionContentInDb(parameters_path,db,attributToSave(vdedf),importId)

def executionInExitingDb(parameters_path,myfile,mysfile,importId):
    db=connexion.connect(parameters_path)
    vdedf=file.vdeToDataframe(myfile)
    vdsdf=file.vdsToDataframe(mysfile)
    # print(vdedf)
    result=otherDimensionContentValue(vdsdf,vdedf)
    d=updateVdsDataframe(vdsdf,result)
    idtable=set.readSetIdFromDb(db,importId)
    d=dimensionContentToSave(d,idtable)

    # #enregistrement de contentDimension sauf les attributs
    writeDimensionContentInDb(parameters_path,db,d,importId)
    # #Enregistrement des dimensions attributs
    writeAttributDimensionContentInDb(parameters_path,db,attributToSave(vdedf),importId)


if __name__=='__main__' :
# paramètres de connexion fichier vde et enfin fichier vds
   
    parameters_path = sys.argv[1]
    myfile = sys.argv[2]
    mysfile = sys.argv[3]
    
    db=connexion.connect(parameters_path)

    vdedf=file.vdeToDataframe(myfile)
    vdsdf=file.vdsToDataframe(mysfile)
    
    result=otherDimensionContentValue(vdsdf,vdedf)
    # print(result)
    d=updateVdsDataframe(vdsdf,result)
    # print(d)
    importId=entete.readImportIdFromDb(db)

    idtable=set.readSetIdFromDb(db,importId)
    d=dimensionContentToSave(d,idtable)
    # #enregistrement de contentDimension sauf les attributs
    writeDimensionContentInDb(db,d,importId)
    # #Enregistrement des dimensions attributs
    writeAttributDimensionContentInDb(db,attributToSave(vdedf),importId)

  
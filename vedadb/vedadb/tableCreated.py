import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import vedadb.connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path=path+"/connectParameters.json"
#Return all tables
def allTable(db):
    return db.get_tables()
#Creation des tables 
def createTable(db):
   
    # db.query("DROP DATABASE IF EXISTS veda")
    # db.query("create database veda")

    db.query("TRUNCATE TABLE entete,template,set,dimensioncontent,vedatable,vedatablecontent,resultat")
     #entete
    db.query("create table if not exists entete "
    "(importid serial primary key, importidveda varchar, gdx2vedaversion varchar, "
    "vedaflavor varchar, dimensions varchar, parentdimensions varchar, "
    "setallowed varchar, fieldsize varchar, notindexed varchar, "
    "defaultvaluedim varchar, fieldseparator varchar, textdelim varchar"
    ")"
    )
    #template
    db.query("create table if not exists template "
    "(templateid serial primary key, templatedescription varchar, templatename varchar, grouptemplate varchar"
    ")"
    )
    #Set
    db.query("create table IF NOT EXISTS set(idset serial " 
    "primary key, typedimensionset varchar, region varchar, "
    "codeset varchar, description varchar, "
    "importid INTEGER REFERENCES entete(importid)"
    ")"
    )
    #Dimension_Content
    # db.query("create table if not exists dimensioncontent "
    # "(iddimensioncontent serial primary key, dimensioncode varchar, "
    # "region varchar, codeset varchar, typedimension varchar, "
    # "descriptiondimensioncode varchar, idset INTEGER REFERENCES set(idset), "
    # "importid  INTEGER REFERENCES entete(importid)"
    # ")"
    # )

    #Dimension_Content
    db.query("create table if not exists dimensioncontent "
    "(iddimensioncontent serial primary key, dimensioncode varchar, "
    "region varchar, codeset varchar, typedimension varchar, "
    "descriptiondimensioncode varchar, idset varchar, "
    "importid  INTEGER REFERENCES entete(importid)"
    ")"
    )
   
    #vedaTable
    db.query("create table if not exists vedatable "
    "(idvedatable serial primary key, nom varchar, "
    "importid  INTEGER REFERENCES entete(importid), "
    "codeoftable  varchar, "
    "description varchar)"
    )
    #vedaTableContent
    db.query("create table if not exists vedatablecontent "
    "(idvedatable integer, "
    "iddimensioncontent integer, "
    "idset integer, "
    "PRIMARY KEY (idvedatable,iddimensioncontent,idset), "
    "importid  INTEGER REFERENCES entete(importid)"
    ")"
    )
    #résultat
    db.query("create table if not exists resultat "
    "(resultid serial primary key, "
    "attribut varchar, "
    "commodity varchar, "
    "process varchar, "
    "periode varchar, "
    "region varchar, "
    "vintage varchar, "
    "timeslice varchar, "
    "userconstraint varchar, "
    "pv varchar, "
    "importid  INTEGER REFERENCES entete(importid)"
    ")"
    )

def execution(parameters_path):
    r=connexion.connect(parameters_path)
    createTable(r)

def dropTableByName(db,tablename):
    myquery="drop table "+tablename
    db.query(myquery)
if __name__ == '__main__':
    # Charger tous les paramètres
    parameters_path = sys.argv[1]
    r=connexion.connect(parameters_path)
    createTable(r)

import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'vedadb'))
import vedadb 
import mypath as mypath
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from vedadb import connexion as connexion
import json
import math
import boto
from filechunkio import FileChunkIO
# full_path = os.path.realpath(__file__)
# path, filename = os.path.split(full_path)
# path=path+"/connectParameters.json"
# sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
# import adress as ping
# path=ping.ping()
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"
ALLOWED_EXTENSIONS = set(['VD', 'VDS', 'VDS', 'VDT'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def deletefile():
    basepath = str(mypath.pathForFile)
    for file in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, file)):
            os.remove(os.path.join(basepath, file))
    result = "no file in" +str(mypath.pathForFile) 
    return result

def get_image():

    UPLOAD_FOLDER=str(mypath.pathForFile)
    print(UPLOAD_FOLDER)
    app = Flask(__name__)
    app.secret_key = "secret key"
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    file = request.files.get('upfile')
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    

"""  
Quand il choisit un Set je fais la recherche dans VDS et pour chaque resultat
 je vais cherche ce qui correspond  dans resultat
A moins que derrière chaque set, je met derrière la liste de VDS correpsondant 
"""
def getOtherResultatFiled(st):
    
    """
    cette fonction permet d'afficher toutes les données liées aux colonnes Attribut, Process and Commodity
     dans la table 
    resultat. Ceci permet de remplir les tables pour permettre à l'utilisateur de faire
    son séléction 
  ex: attribut, periode
    """
    db = connexion.connect(path)
    result = []
    for r in db.query(  # just for example
            "SELECT distinct "+ st +" as code, "+ st+" as description FROM resultat WHERE " + st+ "!='-' AND " + st+ " !='' AND " + st+ " !='NONE'"
            # "SELECT distinct " + st + " FROM resultat"
    ).dictresult():
        result.append(r)
    return result

def getScenario(st):
    
    """
    cette fonction permet d'afficher toutes les données liées aux colonnes Attribut, Process and Commodity
     dans la table 
    resultat. Ceci permet de remplir les tables pour permettre à l'utilisateur de faire
    son séléction 
  ex: attribut, periode
    """
    db = connexion.connect(path)
    result = []
    for r in db.query(  # just for example
            "SELECT distinct importid,"+ st +" as code, "+ st+" as description FROM entete WHERE " + st+ "!='-' AND " + st+ " !='' AND " + st+ " !='NONE'"
            # "SELECT distinct " + st + " FROM resultat"
    ).dictresult():
        result.append(r)
    return result

def whereClauseString(st):
    """
    cette fonction prend en entrée un json qui represente la selection sur laquelle
    l'utilisateur veut faire sa recherche et le transforme en clause where
    """
    stringSearch="("
    for key, value in st.items():
          if (key=="ProcessSET" or key=="UserConstraintSET" or key=="CommoditySET"):
            for s in value:
                r=getSEtWhereClause(s)
                stringSearch=stringSearch+r+ " OR "
            stringSearch=stringSearch.strip(' OR')
            stringSearch=stringSearch+")"
            stringSearch=stringSearch+""
            stringSearch=stringSearch+" AND ("
          elif (key=="importidveda"): 
              #importidveda n'est rien d'autre que scenario. c'est juste pour ne pas toucher le code angular 
              #que j'ai mis importidveda sinon j'aurais dû mettre Scenario
            for s in value:
                r=getScenarioId(s)
                # r=r[0]['importid']
                r='importid='+str(r[0]['importid'])
                stringSearch=stringSearch+r+ " OR "
            stringSearch=stringSearch.strip(' OR')
            stringSearch=stringSearch+")"
            stringSearch=stringSearch+""
            stringSearch=stringSearch+" AND ("

            #     stringSearch=stringSearch+str(r)+ " OR "
            # stringSearch=stringSearch.strip(' OR')
            # stringSearch=stringSearch+")"
            # stringSearch=stringSearch+""
            # stringSearch=stringSearch+" AND ("

          else:
                
            for s in value:
                stringSearch=stringSearch+" "+ key +"='"+s + "' OR "
            stringSearch=stringSearch.strip(' OR')
            stringSearch=stringSearch+")"
            stringSearch=stringSearch+""
            stringSearch=stringSearch+" AND ("
    stringSearch=stringSearch+")"
    stringSearch=stringSearch.replace('AND ()',"")
    print(stringSearch)
    return stringSearch
def read_Search_result(st):

    """
    cette fonction permet de faire la recherche souhaité par le user
    """
    db = connexion.connect(path)
    result = []

    for r in db.query(  # just for example
            "SELECT attribut,commodity,process,periode,region,vintage,timeslice,userconstraint,pv,importid FROM resultat WHERE"+ whereClauseString(st) + " group by attribut,commodity,process,periode,region,vintage,timeslice,userconstraint,pv,importid" 
    ).dictresult():
        result.append(r)
    return result

def getAttributProcessEndCommodity(st):
    """
    cette fonction permet d'afficher toutes les données liées aux colonnes Attribut, Process and Commodity
     dans la table 
    resultat. Ceci permet de remplir les tables pour permettre à l'utilisateur de faire
    son séléction 
    ex st = attribut ou st=vintage....
    """
    db = connexion.connect(path)
    result = []
    for r in db.query(  # just for example
            # "SELECT distinct "+ st +" FROM resultat WHERE " + st+ "!='-' AND " + st+ " !=''"
            "SELECT distinct " + st + " as code ,descriptiondimensioncode as description FROM resultat,dimensioncontent WHERE resultat." + st+ " =dimensioncontent.dimensioncode " 
    ).dictresult():
        result.append(r)
    return result




def getSET(st):
    """
    cette fonction permet d'afficher toutes les données liées à la colonne SET
    resultat. Ceci permet de remplir les tables pour permettre à l'utilisateur de faire
    son séléction 
    ex st = CommoditySET ou st=ProcessSET ou UserConstraintSET
    """
    db = connexion.connect(path)
    result = []
    for r in db.query(  # just for example
            # "SELECT distinct "+ st +" FROM resultat WHERE " + st+ "!='-' AND " + st+ " !=''"
            "SELECT distinct codeset as code,description as description FROM set where typedimensionset= " +"'"+st+"'" 
    ).dictresult():
        result.append(r)
    return result





def getSEtWhereClause(setcode):
    """
    cette fonction permet d'afficher toutes les données liées à la colonne SET
    resultat. Ceci permet de remplir les tables pour permettre à l'utilisateur de faire
    son séléction 
    Il s'agit de prendre un code d'un set de le recherche dans dimensioncontent 
    et de recuperer toutes ces valeurs dans resultat
    ex st = CommoditySET ou st=ProcessSET....
    """
    db = connexion.connect(path)
    result = []
    t=""
    for r in db.query(  # just for example
            # "SELECT distinct "+ st +" FROM resultat WHERE " + st+ "!='-' AND " + st+ " !=''"
            "SELECT distinct dimensioncode, typedimension FROM dimensioncontent where codeset= " +"'"+setcode+"'" 
    ).dictresult():
    #     result.append(r)
    # return result

        t=t+""+r['typedimension'].lower()+"="+"'" +r['dimensioncode'] + "' OR "
    t=t.strip(' OR')
    result.append(t)
    return result[0]

def getScenarioId(importidveda):
    """
    cette fonction permet d'afficher toutes les données liées à la colonne SET
    resultat. Ceci permet de remplir les tables pour permettre à l'utilisateur de faire
    son séléction 
    Il s'agit de prendre un code d'un set de le recherche dans dimensioncontent 
    et de recuperer toutes ces valeurs dans resultat
    ex st = CommoditySET ou st=ProcessSET....
    """
    db = connexion.connect(path)
    result = []
    for r in db.query(  # just for example
            # "SELECT distinct "+ st +" FROM resultat WHERE " + st+ "!='-' AND " + st+ " !=''"
            "SELECT distinct importid FROM entete where importidveda= " +"'"+importidveda+"'" 
    ).dictresult():
        result.append(r)
    return result


if __name__ == "__main__":
    st =   {
    #dimensioncodee in dimensioncontent is Commodity in resultat
    #typedimension in dimensioncontent is process in resultat
    #les sets correspondent à la colonne 
    "commodity": ["AGRCO2","DTCAR"],
   "process": ["AOTETOT","TCAREDSL"],
   "ProcessSET":["DMD","PRE","ELE"],
   "UserConstraintSET":["UC_Const"]
   }
    r=read_Search_result(st)
    print(r)
#   st="DMD"
#   r=getSEtWhereClause(st)
# #   print(json.dumps(r, indent=4, sort_keys=True))
#   print(r)


  
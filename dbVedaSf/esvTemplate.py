import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'vedadb'))
import vedadb 
from vedadb import connexion as connexion
# full_path = os.path.realpath(__file__)
# path, filename = os.path.split(full_path)
# path=path+"/connectParameters.json"
# sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
# import adress as ping
# path=ping.ping()


full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"
"""
affichage des sets à partir des userconstraints de resultats
une fois les userconstraints, je vais les relier à leurs set correspondant avec la Template set
les commodity et les process je les affiche directement à partir de la Template resultat
"""
def save(db,templatedescription,templatename,grouptemplate):
    db.insert('template',templatedescription=templatedescription,templatename=templatename,grouptemplate=grouptemplate)

def executionSavingTemplate(parameters_path,templatedescription,templatename,grouptemplate):
    db=connexion.connect(parameters_path)
    save(db,templatedescription,templatename,grouptemplate)

def saveTemplate(myTemplateRequest):
    executionSavingTemplate(path,
    myTemplateRequest.get("templatedescription"),
    myTemplateRequest.get("templatename"),
    myTemplateRequest.get("grouptemplate")
    )

def getTemplate():
    db=connexion.connect(path)
    result = []

    for r in db.query(  # just for example
            "SELECT * FROM template "
            ).dictresult():
            result.append(r)
    return result

if __name__ == "__main__":
    pass

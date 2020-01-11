import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'vedadb'))
import vedadb 
from vedadb import connexion as connexion

def read_choix_from_Resultat(st,st2):
    db = connexion.connect("connectParameters.json")
    result = []

    for r in db.query(  # just for example
            "SELECT DISTINCT "+ st+ " FROM resultat WHERE"+st2
    ).dictresult():
        result.append(r)
    return result
def read_set(st,st2):
    db = connexion.connect("connectParameters.json")
    result = []

    for r in db.query(  # just for example
            "SELECT DISTINCT "+ st+ " FROM resultat WHERE"+st2
    ).dictresult():
        result.append(r)
    return result
    
if __name__ == "__main__":
    # st=" DISTINCT region"
    # st2=" region!='NONE' and region!='-'"
    st="commodity,userconstraint"
    st2=" commodity!='NONE' and commodity!='-'" 
    r=read_choix_from_Resultat(st,st2)
    print(r)

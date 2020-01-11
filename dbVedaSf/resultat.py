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
def read_AllResultat():
    db = connexion.connect(path)
    result = []

    for r in db.query(  # just for example
            "SELECT * FROM resultat "
    ).dictresult():
        result.append(r)
    return result


def read_one(value):
    db = connexion.connect(path)
    result = []
    for r in db.query(  # just for example
            "SELECT  * FROM  resultat WHERE resultat.attribut="+"'"+value+"';"
    ).dictresult():
        result.append(r)
    return result

    # print(r['idset'])
if __name__ == "__main__":
    d = read_one("VAR_Act")
    print(d)

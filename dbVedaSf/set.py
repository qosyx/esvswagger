import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'vedadb'))
import vedadb 
from vedadb import connexion as connexion
# full_path = os.path.realpath(__file__)
# path, filename = os.path.split(full_path)
# path2=path
# path=path+"/connectParameters.json"
# sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
# import adress as ping
# path=ping.ping()
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"
def read_AllSet():
    db=connexion.connect(path)
    result = []
    for r in db.query(  # just for example
            "SELECT * FROM set "
            ).dictresult():
            result.append(r)
    return result

if __name__ == "__main__":
    d=read_AllSet()
    print(d[0])
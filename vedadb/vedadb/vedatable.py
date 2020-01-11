__all__ = ['vedatable']
import sys
import os
import re
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import vedadb.connexion as connexion
import vedadb.fileToDataframe as file
import vedadb.entete as entete

def saveTable(db,nom,importid,codeoftable,description):
    db.insert('vedatable',nom,importid,codeoftable,description)

def executionSavingTable(parameters_path,nom,importid,codeoftable,description):
    db=connexion.connect(parameters_path)
    saveTable(db,nom,importid,codeoftable,description)

if __name__ == "__main__":
    pass
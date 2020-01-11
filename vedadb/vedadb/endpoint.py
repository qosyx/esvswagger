__all__ = ['endpoint']
import os
import sys
import time


def create(myvdfile,myvdefile,myvdsfile):
    start_time = time.time()
    print("..............")
    os.system("python3 /home/archange/Git/Web/ESV/vedaswaggerui/vedadb/vedadb/entete.py" + 
    " " + "~/VEDA/takatel-veda-api/takatel-veda-db/vedadb/vedadb/connectParameters.json" + " " + myvdfile)
    print("end..............")
    os.system("python3 /home/archange/Git/Web/ESV/vedaswaggerui/vedadb/vedadb/sets.py" + 
    " " + "~/VEDA/takatel-veda-api/takatel-veda-db/vedadb/vedadb/connectParameters.json" + " " + myvdefile)
    print("..............")
    os.system("python3 /home/archange/Git/Web/ESV/vedaswaggerui/vedadb/vedadb/dimensionContent.py" + 
    " " + "~/VEDA/takatel-veda-api/takatel-veda-db/vedadb/vedadb/connectParameters.json" + " " + myvdefile + " " + myvdsfile)
    print("end ..............")
    os.system("python3 /home/archange/Git/Web/ESV/vedaswaggerui/vedadb/vedadb/resultat.py" + 
    " " + "~/VEDA/takatel-veda-api/takatel-veda-db/vedadb/vedadb/connectParameters.json" + " " + myvdfile)
    print("donnée bien chargée")
    print("Temps d execution : %s secondes ---" % (time.time() - start_time))
if __name__ == "__main__":
    create("/home/archange/VEDA/base/DemoS_012.VD","/home/archange/VEDA/base/DemoS_012.VDE","/home/archange/VEDA/base/DemoS_012.VDS")
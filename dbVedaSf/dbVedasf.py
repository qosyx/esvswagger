# __all__ = ['endpoint']
from rq import Queue
from rq.job import Job
import time
import threading
import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'vedadb'))
import vedadb 
import shutil
from vedadb import connexion as connexion
import socket
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
from worker import conn
# sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
# import adress as ping
# path=ping.ping()
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path = path+"/connectParameters.json"
def getJobStatus(jobid):
    """
    get job queue status
    """
    job = Job.fetch(jobid, connection=conn)
    return job.get_status()

def createmyq(vedafile):
    
    # q = Queue('high', connection=conn)
    q = Queue('high', connection=conn)
    job = q.enqueue(vedadb.entete.execution,path,vedafile.get("myvdfile"))

    return job.get_id()

def CreateByqueue(vedafile):
    """
    Create database by use queue
    """
    # q = Queue('high', connection=conn)
    q = Queue('high', connection=conn)
    job = q.enqueue(create, vedafile)
    jobid=job.get_id()
    return job.get_id()
    # print(job.get_status())

def createToexitingDbByqueue(vedafile):
    
    # q = Queue('high', connection=conn)
    q = Queue('high', connection=conn)
    job = q.enqueue(createToexitingDb, vedafile)
    return job.get_id()

def create(vedafile):
    # vedadb.tableCreated.execution(path)
    vedadb.entete.execution(path,vedafile.get("myvdfile"))
    vedadb.sets.execution(path,vedafile.get("myvdefile"))
    vedadb.dimensionContent.execution(path,vedafile.get("myvdefile"),vedafile.get("myvdsfile"))
    vedadb.resultat.execution(path,vedafile.get("myvdfile"))
    return vedadb.entete.readImportIdFromDb(vedadb.connexion.connect(path))
    
def createToexitingDb(vedafile):
    vedadb.entete.execution(path,vedafile.get("myvdfile"))
    vedadb.sets.execution(path,vedafile.get("myvdefile"))
    vedadb.dimensionContent.execution(path,vedafile.get("myvdefile"),vedafile.get("myvdsfile"))
    vedadb.resultat.execution(path,vedafile.get("myvdfile"))
    return vedadb.entete.readImportIdFromDb(vedadb.connexion.connect(path))

def createfromexitingDb(vedafile,importID):
    vedadb.entete.execution(path,vedafile.get("myvdfile"))
    vedadb.sets.executionInExitingDb(path,vedafile.get("myvdefile"),importID)
    vedadb.dimensionContent.executionInExitingDb(path,vedafile.get("myvdefile"),vedafile.get("myvdsfile"),importID)
    vedadb.resultat.executionInExitingDb(path,vedafile.get("myvdfile"),importID)
    return importID




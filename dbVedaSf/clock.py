import os,sys
# from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.background import BackgroundScheduler
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import dbVedasf as dbVedasf
from worker import conn
from sched import scheduler
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
from worker import conn
jobid=""
@sched.scheduled_job('interval', seconds=3)
def timed_job():
    
    if (jobid!=""):
        print('This job is run every three minutes.')
        print(dbVedasf.getJobStatus(jobid))
        return dbVedasf.getJobStatus(jobid)
    else:
        pass
    
def getJobStatus(jobid):
    """
    get job queue status
    """
    job = Job.fetch(jobid, connection=conn)
    jobid = job.get_status()
    timed_job()
    return job.get_status()





# @sched.scheduled_job('interval', seconds=1)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched.start()

# # @sched.scheduled_job('interval',  hours=5)
# def get_jobStatus():
#     scheduler.add_job(dbVedasf.getJobStatus, 'interval', seconds=3)



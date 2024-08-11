import schedule
import time
from datetime import datetime
from .models import Job

def run_job(job_id):
    job = Job.objects.get(id=job_id)
    job.last_run = datetime.now()
    # Implement the job logic
    job.save()

def schedule_jobs():
    jobs = Job.objects.filter(is_active=True)
    for job in jobs:
        if job.interval == 'daily':
            schedule.every().day.at("10:00").do(run_job, job_id=job.id)
        elif job.interval == 'weekly':
            schedule.every().monday.at("10:00").do(run_job, job_id=job.id)
        # Add more intervals as needed

def run_scheduler():
    schedule_jobs()
    while True:
        schedule.run_pending()
        time.sleep(1)


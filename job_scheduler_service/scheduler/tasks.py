from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Job
from django.core.mail import send_mail
import math

@shared_task
def execute_job(job_id):
    try:
        print(f"Received job_id: {job_id}")  # Debugging line
        job = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        print(f"Job with id {job_id} does not exist.")
        return
    except Exception as e:
        print(f"Error retrieving job: {e}")
        return

    # Update last_run time
    job.last_run = timezone.now()
    
    # Job Logic: Send Email Notification
    if job.name == "Send Email Notification":
        send_email_notification()

    # Job Logic: Number Crunching
    elif job.name == "Number Crunching":
        result = perform_number_crunching()
        print(f"Number Crunching Result: {result}")

    # Calculate and update next_run for recurring tasks
    if job.interval == 'weekly':
        job.next_run = job.last_run + timedelta(weeks=1)
    elif job.interval == 'hourly_for_today':
        job.next_run = job.last_run + timedelta(hours=1)
    
    # Save the updated last_run and next_run values
    job.save()
    print(f"Executed job: {job.name}")

def send_email_notification():
    send_mail(
        'Scheduled Email Notification',
        'This is a scheduled email sent by the job scheduler.',
        'burhanmohammad1234@outlook.com',
        ['burhanmohammad1234@outlook.com'],
        fail_silently=False,
    )

def perform_number_crunching():
    # Calculate the sum of the first 1000 factorial numbers
    total = sum(math.factorial(i) for i in range(1, 1001))
    return total



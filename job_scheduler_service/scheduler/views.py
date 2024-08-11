from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.utils import timezone
from datetime import timedelta
import json

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = serializer.save()
        
        # job based on the interval specified
        if job.interval == 'weekly':
            # run every Monday at 10:00 AM
            schedule, _ = CrontabSchedule.objects.get_or_create(
                minute='0',
                hour='10',
                day_of_week='1',
            )
            job.next_run = timezone.now() + timedelta(days=(7 - timezone.now().weekday()))

        elif job.interval == 'hourly_for_today':
            # run every hour for today
            schedule, _ = CrontabSchedule.objects.get_or_create(
                minute='0',
                hour='*',
            )
            job.next_run = timezone.now() + timedelta(hours=1)

        # updated next_run value before creating the PeriodicTask
        job.save()

        # periodic task
        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'Execute {job.name} (ID: {job.id})',
            task='scheduler.tasks.execute_job',
            args=json.dumps([job.id]),
        )

class JobRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer




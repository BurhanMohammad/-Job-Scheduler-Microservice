from django.core.management.base import BaseCommand
from scheduler.scheduler import run_scheduler

class Command(BaseCommand):
    help = 'Starts the job scheduler'

    def handle(self, *args, **kwargs):
        run_scheduler()






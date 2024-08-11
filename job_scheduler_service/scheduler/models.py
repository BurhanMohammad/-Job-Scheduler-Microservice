from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)
    last_run = models.DateTimeField(null=True, blank=True)
    next_run = models.DateTimeField(null=True, blank=True)
    interval = models.CharField(max_length=50)  # 'daily', 'weekly', 'monthly'
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
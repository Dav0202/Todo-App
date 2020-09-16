from django.db import models
from  django.utils import timezone
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    priority = models.TextField()
    date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

    def __str__(self):
        return self.name

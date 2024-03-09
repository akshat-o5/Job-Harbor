from django.db import models
from django.utils import timezone
from django.utils.timezone import now


# Create your models here.

class Seasoned(models.Model):
    sno = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    postTime = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    experience = models.CharField(max_length=50)
    link = models.CharField(max_length=200)


    def __str__(self):
        return self.company + " " + self.profile
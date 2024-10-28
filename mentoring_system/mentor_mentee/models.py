from django.db import models

# Create your models here.
class Mentor(models.Model):
   Staff_id = models.IntegerField()
   Name = models.TextField()
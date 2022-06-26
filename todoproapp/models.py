from django.db import models

# Create your models here.
class Todomodel(models.Model):
    content = models.TextField()

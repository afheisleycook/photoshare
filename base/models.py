from django.db import models
class PhotoUser(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    username = models.CharField(max_length=100)
    password = models.TextField(max_length=200)

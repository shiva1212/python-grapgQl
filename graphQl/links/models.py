from django.db import models

# Create your models here.
class Link(models.Model):
    url = model.URLField()
    description =  models.TextField(blank=True)
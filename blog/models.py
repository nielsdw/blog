from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=32)
    slug = models.CharField(max_length=32)
    summary = models.CharField(max_length=256)
    content = models.CharField(max_length=4096)
    createdOn = models.DateTimeField(auto_now=True)
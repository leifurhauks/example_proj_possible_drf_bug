from django.db import models

class Profile(models.Model):
    description = models.TextField()
    tags = models.ManyToManyField('profiles.Tag')


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


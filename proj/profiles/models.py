from django.db import models

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    description = models.TextField()
    tags = models.ManyToManyField('profiles.Tag')


class Tag(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()


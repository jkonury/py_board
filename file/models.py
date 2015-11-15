from django.contrib.auth.models import User
from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='documents/%Y/%m/%d')
    name = models.CharField(max_length=200)
    size = models.IntegerField()
    user = models.ForeignKey(User)
    ip = models.GenericIPAddressField()

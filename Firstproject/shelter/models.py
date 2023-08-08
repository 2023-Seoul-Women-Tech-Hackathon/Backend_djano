from django.conf import settings

from django.db import models

class AreaCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    def __str__(self):return self.code
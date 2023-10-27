# spinner_app/models.py

from django.db import models

class Choice(models.Model):
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.body

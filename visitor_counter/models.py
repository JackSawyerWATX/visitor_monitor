# visitor_counter/models.py
from django.db import models

class Visitor(models.Model):
    count = models.IntegerField(default=0)
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
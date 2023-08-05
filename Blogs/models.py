from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class ContactTb(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.name}, {self.email}"
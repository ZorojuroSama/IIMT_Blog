from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class ContactTb(models.Model):
    name = models.CharField(max_length=50,)
    email = models.EmailField(max_length=70)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    message = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True, default=datetime.now())
    
    def __str__(self) -> str:
        return f"{self.name} - {self.email}"
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    msg = models.TextField()
    msg_date_time = models.DateTimeField(auto_now_add=True)
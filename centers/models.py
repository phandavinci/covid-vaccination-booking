from django.db import models
from user.models import UserSignIn
from datetime import time, date, datetime
# Create your models here.

class centersdb(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mobileno = models.CharField(max_length=10)
    line1 = models.CharField(max_length=50)
    line2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    dosage = models.IntegerField()
    vacancy = models.IntegerField()
    slots = models.IntegerField()
    whfrom = models.TimeField()
    whto = models.TimeField()
    created = models.DateField(auto_now_add=True, verbose_name='EntryDate')
    def __str__(self):
        return str(self.id)
    
class entries(models.Model):
    centerid = models.ForeignKey(centersdb, on_delete=models.CASCADE)
    userno = models.ForeignKey(UserSignIn, on_delete=models.CASCADE)
    slot = models.IntegerField()
    entrydate = models.DateField(default=date.today, verbose_name='EntryDate')
    def __str__(self):
        return str(self.userno)
    

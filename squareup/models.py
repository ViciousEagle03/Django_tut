from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone

# Create your models here.
# After making a model we need to do new migrations

class Group(models.Model):
    # Here we are inherating from models and this will change the standard python class to django model
    host = models.ForeignKey(User , on_delete = models.SET_NULL,null=True)
    Grpname = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True) 
    participants = models.ManyToManyField(User,related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return self.Grpname
    
class GroupExpense(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE,default=1)
    participants = models.ForeignKey(User , on_delete = models.SET_NULL,null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True , blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return str(self.participants)
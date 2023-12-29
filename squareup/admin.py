from django.contrib import admin

# Register your models here.
from .models import Group,GroupExpense

admin.site.register(Group)
admin.site.register(GroupExpense)
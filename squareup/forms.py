from django.forms import ModelForm
from .models import Group,GroupExpense

class GroupForm(ModelForm):
    class Meta:
       model = Group
       fields = ['host','Grpname','description']
       
class ExpenseForm(ModelForm):
    class Meta:
        model = GroupExpense
        fields = ['group','participants','amount','description']
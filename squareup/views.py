from django.shortcuts import render , redirect
from .forms import GroupForm,ExpenseForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.forms import UserCreationForm
from .models import GroupExpense , Group
# Create your views here. / handlers

def loginPage(request):
    Page ='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    
    if request.method == "POST" :
        username = request.POST.get("username").lower()
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:  # noqa: E722
            messages.error(request,"The User does not exist")
            
        user = authenticate(request , username=username , password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request , "The username or password does not exist")
            
            
    context={'Page' : Page}
    return render(request ,'squareup/login_register.html' ,context)

def logoutUser(request):
    logout(request)
    return redirect("home")
    
def registerPage(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')
            
    context = {'form' : form}
    return render(request , 'squareup/login_register.html',context)
    
def home(request):
    return render(request , 'squareup/home.html')

def group(request):
    if request.method == "POST":
        groupname = request.POST.get("groupname")
        return redirect ('group_expense',pk=groupname)
    return render(request , 'squareup/group.html' ,)


@login_required(login_url='loginPage')
def newgroup(request): 
    form = GroupForm()
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_expense',pk = request.POST.get('Grpname'))
            
    context = {'form':form}
    return render(request , 'squareup/new_group.html',context)


def add_expense(request):
    form = ExpenseForm()
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            expense_instance = form.save()
            group_name = expense_instance.group.Grpname
            amount = form.cleaned_data.get('amount')
            participants = form.cleaned_data.get('participants')
            participants_id = participants.id
            print("yahoo")
            #return redirect('group_expense', pk = str(group_name), amount=str(amount), participants=str(participants_id) )
            return redirect('group_expense' , pk = group_name)
    
    context = {'form' : form}
    return render(request , 'squareup/add_expense.html' , context)
            
def group_expense(request,pk):
    amount =[]
    grp_expenses = GroupExpense.objects.filter(group__Grpname=pk)
    # simplified version of 
    # group = Group.objects.get(Grpname=pk)
    # group_expenses = GroupExpense.objects.filter(group=group) 033 40904195
    
    context = {'pk': pk, 'grp_expenses':grp_expenses}
    return render(request , 'squareup/group_expense.html' , context)
    
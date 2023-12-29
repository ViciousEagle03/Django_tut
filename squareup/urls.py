from django.urls import path
from . import views

urlpatterns = [
    path('loginPage/' , views.loginPage , name='loginPage'),
    path('logout/' , views.logoutUser,name='logout'),
    path('register/' , views.registerPage,name='register'),
    path('', views.home ,name = 'home'),
    path('grp/', views.group , name ='group'),
    path('create-group/',views.newgroup, name ='create-group'),
    path('group_expense/<str:pk>/',views.group_expense,name ='group_expense'),
    path('addexpense/' ,views.add_expense,name ='addexpense')

]

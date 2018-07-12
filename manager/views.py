from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Tasks, Employee
# Create your views here.
@login_required
def index(request):
    Currenttasks = Tasks.objects.all()
    Employees = Employee.objects.all()
    return render(request,'manager/dashboard.html',{'Currenttasks':Currenttasks, 'Employees':Employees})

@login_required
def user_profile(request):
    return render(request,'manager/user_profile.html')

@login_required
def managecashiers(request):
    users = User.objects.all()
    return render(request,'manager/managecashiers.html',{'users':users})

@login_required
def transaction(request):
    return render(request,'manager/transaction.html')

@login_required
def addtask(request):
    if request.method =='POST':
         newtask = Tasks()
         newtask.Task = request.POST['task']
         newtask.save()
         return HttpResponseRedirect(reverse('manager:index'))


@login_required
def addEmployee(request):
    if request.method =='POST':
        newEmployee = Employee()
        newEmployee.First_Name = request.POST['First_Name']
        newEmployee.Last_Name = request.POST['Last_Name']
        newEmployee.Address = request.POST['Address']
        newEmployee.Contact = request.POST['Contact']
        newEmployee.Country = request.POST['Country']
        newEmployee.Salary = request.POST['Salary']
        newEmployee.save()

        return HttpResponseRedirect(reverse('manager:index'))

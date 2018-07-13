from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Tasks, Employee
from cashier.models import Products , Sales , Purchases
from django.db.models import Count , Sum , Avg
from django.db.models.functions import TruncMonth, TruncYear
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
    sales_per_month = Sales.objects.annotate(month=TruncMonth('date_of_sale')).values('month').annotate(total_sales=Sum('total_amount'))
    purchases_per_month = Purchases.objects.annotate(month=TruncMonth('date_of_purchase')).values('month').annotate(total_purchases=Sum('total'))
    print(purchases_per_month)
    return render(request,'manager/transaction.html',{'sales_per_month':sales_per_month, 'purchases_per_month':purchases_per_month})

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

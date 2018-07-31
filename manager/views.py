from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from .models import Tasks, Employee
from .functions import save_employee, findsalespermonth, findpurchasespermonth, findsalesoverpeiod, findpurchasesoverpeiod
from cashier.models import Products , Sales , Purchases
from datetime import datetime, date
from django.contrib import messages
from django.db.models import Count , Sum , Avg, Q, F, Min
from django.db.models.functions import TruncMonth, TruncYear



# Create your views here.
@login_required
def index(request):
    username = request.session['username']
    Currenttasks = Tasks.objects.all()
    Employees = Employee.objects.all()
    return render(request,'manager/dashboard.html',{'Currenttasks':Currenttasks, 'Employees':Employees,'username':username})

@login_required
def user_profile(request):
    username = request.session['username']
    return render(request,'manager/user_profile.html',{'username':username})

@login_required
def managecashiers(request):
    username = request.session['username']
    users = User.objects.all()
    return render(request,'manager/managecashiers.html',{'users':users,'username':username})

@login_required
def transaction(request):
    username = request.session['username']
    sales_per_month = findsalespermonth()
    purchases_per_month = findpurchasespermonth()

    # print(purchases_per_month)
    return render(request,'manager/transaction.html',{'sales_per_month':sales_per_month, 'purchases_per_month':purchases_per_month,'username':username})

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
        save_employee(request.POST)
        return HttpResponseRedirect(reverse('manager:index'))

@login_required
def deleteTask(request, taskId):
    Tasks.objects.get(id=taskId).delete()
    return HttpResponseRedirect(reverse('manager:index'))

@login_required
def managestock(request):
    context = {}
    if request.method=='GET':
            return render(request,'manager/viewstock.html')
    else:
        from_date = request.POST['from']
        # to_date = request.POST['to']
        to_date =  str(date.today())

        sales_status_as_of = findsalesoverpeiod(from_date , to_date)
        product_status_as_of = findpurchasesoverpeiod(from_date, to_date)
        # red=product_status_as_of.filter(name='Coco-butter')
        items=[]
        # i=0
        for item in Products.objects.annotate(min_purchasedate = Min('purchases__date_of_purchase')).filter(min_purchasedate__lte = from_date ):
            #filter from the product_status_as_of
            purchase_status = product_status_as_of.filter(name = item.name)

            #filter from the sales_status_as_of
            sale_status = sales_status_as_of.filter(name = item.name)

            #product has both purchase_status and sale_status in that period
            if (purchase_status[0]['purchases_as_of'] is not None) and (sale_status[0]['sales_as_of'] is not None):
                    items.append({'name':item.name ,'selling_price':item.selling_price,'available_quantity': (item.available_quantity) - (purchase_status[0]['purchases_as_of'] + sale_status[0]['sales_as_of']) })


            #product has only purchase_status in that period
            elif (purchase_status[0]['purchases_as_of'] is not None):
                print('excetuted elseif1')
                items.append({'name':item.name ,'selling_price':item.selling_price,'available_quantity': (item.available_quantity) -(purchase_status[0]['purchases_as_of']) })

                #product has only sale_status in that period
            elif (sale_status[0]['sales_as_of'] is not None):
                print('excetuted elseif2')
                items.append({'name':item.name ,'selling_price':item.selling_price,'available_quantity': (item.available_quantity) -(sale_status[0]['sales_as_of']) })

            #if has none
            else:
                print('excetuted else')
                items.append({'name':item.name ,'selling_price':item.selling_price,'available_quantity': (item.available_quantity) })

        print(items)
        print(Products.objects.annotate(min_purchasedate = Min('purchases__date_of_purchase')).filter(min_purchasedate__lte = from_date ).count())
        if items:
            return render(request,'manager/viewstock.html',{'items': items})
        else:
            context['error']='No results found'
            return render(request,'manager/viewstock.html',{'messages':context['error']})

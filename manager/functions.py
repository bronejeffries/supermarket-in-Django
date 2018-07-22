from cashier.models import Products , Sales , Purchases
from .models import  Employee
from django.db.models import Count , Sum , Avg, Q, F
from django.db.models.functions import TruncMonth, TruncYear

#save_employee to database
def save_employee(details):
    newEmployee = Employee()
    newEmployee.First_Name = details['First_Name']
    newEmployee.Last_Name = details['Last_Name']
    newEmployee.Address = details['Address']
    newEmployee.Contact = details['Contact']
    newEmployee.Country = details['Country']
    newEmployee.Salary = details['Salary']
    newEmployee.save()

#find sales per month
def findsalespermonth():
    return Sales.objects.annotate(month=TruncMonth('date_of_sale')).values('month').annotate(total_sales=Sum('total_amount'))
#find purchases per month
def findpurchasespermonth():
    return Purchases.objects.annotate(month=TruncMonth('date_of_purchase')).values('month').annotate(total_purchases=Sum('total'))


def findsalesoverpeiod(from_date, to_date):
    sales_as_of =  Sum('sales__quantity_sold', filter=Q(sales__date_of_sale__range=(from_date , to_date)),distinct=True)
    return Products.objects.distinct().annotate(sales_as_of = sales_as_of).values('sales_as_of','name','available_quantity')

def findpurchasesoverpeiod(from_date, to_date):
    purchases_as_of = Sum('purchases__quantity_purchased',filter=Q(purchases__date_of_purchase__range=(from_date , to_date)),distinct=True)
    return Products.objects.distinct().annotate(purchases_as_of = purchases_as_of).values('purchases_as_of','name','available_quantity')

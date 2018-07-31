
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Products , Sales , Purchases
from datetime import date

from .functions.cashierfunctions import functions
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):

    products = Products.objects.all()
    username = request.session['username']
    # return render(request, '')
    return render(request,'cashier/index.html',{ 'products' : products, 'username':username})

@login_required
def enter_reciept(request):
    username = request.session['username']
    if request.method!='GET':
            prod = Products.objects.all()
            item_name = request.POST.getlist('item_name')
            item_cost_price =request.POST.getlist('item_cost_price')
            item_quantity =request.POST.getlist('item_quantity')
            today = str(date.today())
            req=request.POST
            for i in range(len(item_name)):
                st = item_name[i].strip()
                product = Products.objects.get(name = st)
                product.available_quantity = int(product.available_quantity) + int(item_quantity[i])
                product.save()

                # update the database
                try:
                    selected_product_purchase = product.purchases_set.get(date_of_purchase=today)
                except (KeyError, Purchases.DoesNotExist):
                    product.purchases_set.create(Cost_price = int(item_cost_price[i]),quantity_purchased = int(item_quantity[i]),total=(int(item_cost_price[i])* int(item_quantity[i])))
                else:
                    selected_product_purchase.quantity_purchased = int(selected_product_purchase.quantity_purchased) + int(item_quantity[i])
                    selected_product_purchase.item_cost_price = int(item_cost_price[i])
                    selected_product_purchase.total += (int(item_quantity[i])*int(item_cost_price[i]))
                    selected_product_purchase.save()
            # return HttpResponseRedirect(reverse('cashier:enter_reciept'))
            return render(request,'cashier/enter_reciept.html',{'products':prod, 'req':req,'username':username})

    else:
        prod = Products.objects.all()
        return render(request,'cashier/enter_reciept.html',{'products':prod,'username':username})

@login_required
def expenses(request):
    username = request.session['username']
    if request.method=='GET':
        return render(request,'cashier/expenses.html',{'username':username})
    else:

        return HttpResponseRedirect(reverse('cashier:expenses'))

@login_required
def add_sales(request):

    if request.method!='GET':
        # prod = Products.objects.all()
        item = request.POST.getlist('item')
        quantity=request.POST.getlist('quantity')
        total_amount=request.POST.getlist('total')
        today = str(date.today())
        st=''
        for i in range(len(item)):
            st = item[i].strip()
            product = Products.objects.get(name = st)
            product.available_quantity = int(product.available_quantity) - int(quantity[i])
            product.save()
            # update the database
            try:
                selected_product_sale = product.sales_set.get(date_of_sale=today)
            except (KeyError, Sales.DoesNotExist):
                product.sales_set.create(quantity_sold = quantity[i], total_amount=total_amount[i])
            else:
                selected_product_sale.quantity_sold = int(selected_product_sale.quantity_sold) + int(quantity[i])
                selected_product_sale.total_amount = int(selected_product_sale.total_amount) + int(total_amount[i])
                selected_product_sale.save()
        # return render(request,'cashier/index.html',{'products':prod ,'st': st})
        return HttpResponseRedirect(reverse('cashier:index',))

@login_required
def add_item(request):
    username = request.session['username']
    if request.method=='GET':
        return render(request,'cashier/add_item.html',{'username':username})

    else:
        newItem = functions.addnewitem(request.POST['item_name'],request.POST['item_selling_price'])
        if newItem:
            return HttpResponseRedirect(reverse('cashier:enter_reciept'))


@login_required
def uploadcsvfile(request):
    uploadedfile= request.FILES['uploadedcsvfile']
    functions.handle_uploaded_file(uploadedfile)
    return HttpResponseRedirect(reverse('cashier:add_item'))

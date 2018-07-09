from django.conf.urls import url
from . import views
from django.conf.urls.static import static

app_name = 'cashier'

urlpatterns = [
#cashier/
    url(r'^$',views.index,name='index'),
    url(r'^enter_reciept/$',views.enter_reciept,name='enter_reciept'),
    url(r'^expenses/$',views.expenses, name='expenses'),
    url(r'^add_sales/$',views.add_sales, name='add_sales'),
    url(r'^enter_reciept/add_item/$',views.add_item, name='add_item'),

]

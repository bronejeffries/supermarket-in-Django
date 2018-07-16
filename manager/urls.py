from django.conf.urls import url
from . import views
from django.conf.urls.static import static

app_name = 'manager'

urlpatterns = [
#cashier/
    url(r'^$',views.index,name='index'),
    url(r'^user/$',views.user_profile,name='user_profile'),
    url(r'^managecashiers/$',views.managecashiers,name='manage_cashiers'),
    url(r'^transaction/$',views.transaction,name='transaction'),
    url(r'^addtask/$',views.addtask,name='addTask'),
    url(r'^addEmployee/$',views.addEmployee,name='addEmployee'),
    url(r'^delete/(?P<taskId>[0-9]+)/$',views.deleteTask,name='deleteTask'),



]

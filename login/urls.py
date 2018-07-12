# from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import user_logout,user_login

app_name = 'login'

urlpatterns = [
        url(r'^$',user_login,name='login'),
        url(r'^logout',user_logout,name='logout'),
]

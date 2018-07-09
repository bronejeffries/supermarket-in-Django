from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'manager/dashboard.html')

def user_profile(request):
    return render(request,'manager/user_profile.html')

def managecashiers(request):
    return render(request,'manager/managecashiers.html')

def transaction(request):
    return render(request,'manager/transaction.html')

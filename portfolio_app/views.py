from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'portfolio_home.html')


def aboutme(request):
    return render(request,'aboutme.html',{ 
        'Fname': 'Shahariya',
        'Lname': 'Mamun'
        })
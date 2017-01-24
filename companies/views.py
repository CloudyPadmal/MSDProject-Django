from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    info = {'principal': "Company", 'admin': False, 'action_url': "", 'register_url': "companies:company-register"}
    return render(request, 'users/logins/main_login.html', info)

def register(request):
    info = {'register': True, 'action_url': "companies:company-do-register"}
    return render(request, 'users/logins/register_user.html', info)

def do_register(request):
    # Create a company
    company = Company()
    return HttpResponse(company.title)


def show(request, loginID):
    return HttpResponse(loginID)

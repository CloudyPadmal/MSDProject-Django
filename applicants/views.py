from django.http import HttpResponse
from django.shortcuts import render
from .models import Preferences, Applicant

def login(request):
    info = {'principal': "Student", 'admin': False, 'action_url': "", 'register_url': "users:user-register"}
    return render(request, 'users/logins/main_login.html', info)

def register(request):
    preferences = Preferences()
    preferences.ai = True
    info = {'register': True, 'preferences': preferences, 'action_url': "users:user-do-register"}
    return render(request, 'users/logins/register_user.html', info)

def do_register(request):
    # Create a user
    user = Applicant()
    user.name = request.POST['name']
    user.surname = request.POST['surname']
    user.email = request.POST['email']
    user.indexNumber = request.POST['indexNumber']
    user.telephone = request.POST['telephone']
    user.gender = request.POST['gender']
    return HttpResponse(request.POST['gender'])


def show(request, index):
    return HttpResponse(index)

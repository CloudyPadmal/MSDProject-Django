from django.http import HttpResponse
from django.shortcuts import render
from .models import Preferences, Applicant
from .forms import UserForm, PreferenceForm

def login(request):
    info = {'principal': "Student", 'admin': False, 'action_url': "", 'register_url': "users:user-register"}
    return render(request, 'users/logins/main_login.html', info)

def register(request):
    if request.method == 'POST':
	# Create a form to validate data
	form = UserForm(request.POST)
	prefForm = PreferenceForm(request.POST)
	# Check for validation errors
	if form.is_valid() and prefForm.is_valid():
	    preferences = prefForm.save()
	    applicant = Applicant(
		name = form.cleaned_data['name'],
		surname = form.cleaned_data['surname'],
		email = form.cleaned_data['email'],
		indexNumber = form.cleaned_data['indexNumber'],
		telephone = form.cleaned_data['telephone'],
		gpa = form.cleaned_data['gpa'],
		aboutMe = form.cleaned_data['aboutMe'],
		gender = form.cleaned_data['gender']
	    )
	    applicant.preferences = preferences
	    applicant.save()
	info = {'register': True, 'action_url': "users:user-register", 'form': form, 'prefForm': prefForm,}
    else:
	form = UserForm()
	prefForm = PreferenceForm()
        info = {'register': True, 'action_url': "users:user-register", 'form': form, 'prefForm': prefForm,}
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

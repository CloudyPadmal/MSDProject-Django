from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import Applicant, Preferences

class UserForm(forms.ModelForm):

    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput,)
    confirmPassword = forms.CharField(widget=forms.PasswordInput, label="Confirm", required=True,)

    class Meta:
	model = Applicant
	exclude = ['vacancy_A', 'vacancy_B', 'vacancy_C', 'appeal_A', 'appeal_B', 'appeal_C', 'awarded',]
	labels = {'gender': _('Sex'),}
	help_texts = {'indexNumber': '14XXXXZ',}

class PreferenceForm(forms.ModelForm):
    class Meta:
	model = Preferences
	fields = '__all__'

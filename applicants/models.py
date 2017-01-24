from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Gender Choices
GENDER = (
	('M', 'Male'),
	('F', 'Female'),
    )

# Custom Validators
def gpaValidator(gpa):
    if gpa > 4.2 or gpa < 1.0:
	raise ValidationError(_('Invalid GPA!'), params={'gpa': gpa})

def indexValidator(index):
    if len(index) != 7:
	raise ValidationError(_('Invalid Index Number!'), params={'index': index})


class Preferences(models.Model):
    ai = models.BooleanField('Artificial Intelligence', default=False)
    antenna = models.BooleanField('Antennas', default=False)
    arduino = models.BooleanField('Arduino', default=False)
    automation = models.BooleanField('Automation', default=False)
    biomechanics = models.BooleanField('Bio Mechanics', default=False)
    biomedical = models.BooleanField('Bio Medical', default=False)
    circuits= models.BooleanField('Circuits', default=False)
    fpga = models.BooleanField('FPGA', default=False) 
    imageProcessing = models.BooleanField('Image Processing', default=False)
    iot = models.BooleanField('Internet of Things', default=False)
    robotics = models.BooleanField('Robotics', default=False)
    networking = models.BooleanField('Networking', default=False)
    processorDesign = models.BooleanField('Processor Design', default=False)
    programming = models.BooleanField('Programming', default=False)
    telecom = models.BooleanField('Telecommunication', default=False)
    semiconductors = models.BooleanField('Semi-Conductors', default=False)
    signalProcessing = models.BooleanField('Signal Processing', default=False)
    wifi = models.BooleanField('WiFi Technology', default=False)

    def __str__(self):
	return "Student Preferences"

    class Meta:
	verbose_name = "Preference"
	verbose_name_plural = "Preferences"

    
class Applicant(models.Model):
    name = models.CharField('First Name', max_length=100, blank=False)
    surname = models.CharField('Surname', max_length=100, blank=False)
    gender = models.CharField(choices=GENDER, max_length=1)
    indexNumber = models.CharField('Index', max_length=7, validators=[indexValidator], unique=True)
    email = models.EmailField('Email', blank=False)
    telephone = models.CharField('Telephone', max_length=15, blank=False)
    gpa = models.DecimalField(decimal_places=4, max_digits=5, validators=[gpaValidator])
    aboutMe = models.TextField('About Me', blank=False)
    vacancy_A = models.IntegerField(verbose_name="First Choice", default=0)
    vacancy_B = models.IntegerField(verbose_name="Second Choice", default=0)
    vacancy_C = models.IntegerField(verbose_name="Third Choice", default=0)
    appeal_A = models.IntegerField(verbose_name="First Appeal", default=0)
    appeal_B = models.IntegerField(verbose_name="Second Appeal", default=0)
    appeal_C = models.IntegerField(verbose_name="Third Appeal", default=0)
    awarded = models.IntegerField(verbose_name="Awarded Vacancy", default=0)
    preferences = models.ForeignKey(Preferences, on_delete=models.CASCADE, null=True)

    def __str__(self):
	return self.name + " " + self.surname


class Company(models.Model):
    aboutUs = models.TextField('About', blank=False)
    address = models.CharField('Company Address', max_length=250)
    companyName = models.CharField('Company', max_length=200)
    email = models.EmailField('Email', blank=False)
    loginID = models.CharField('Login ID', max_length=100)
    positions = models.IntegerField('Vacancies Posted', default=0)
    telephone = models.CharField('Telephone', blank=False, max_length=11)

    def __str__(self):
	return self.companyName


class Vacancy(models.Model):
    is_open = models.BooleanField('Availability', default=True)
    is_awarded = models.BooleanField('Awarded', default=False)
    title = models.CharField('Title', max_length=100)    
    pub_date = models.DateTimeField('Published Date')
    salary = models.IntegerField('Salary', default=0)
    description = models.TextField('Job Description', blank=False, null=True)
    sub_description = models.TextField('More..', blank=False, null=True)
    choice = models.IntegerField('Choice', default=0)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    preferences = models.ForeignKey(Preferences, on_delete=models.CASCADE, null=True)

    def __str__(self):
	return self.title

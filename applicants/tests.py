from django.test import TestCase
from .models import Applicant, Preferences, Vacancy

class ApplicantTests(TestCase):

    def test_create_a_valid_new_applicant(self):
	# Creation
	applicant = Applicant()
	applicant.name="Padmal"
	applicant.surname="Knight"
	applicant.gender="M"
	applicant.indexNumber="140427D"
	applicant.email="blog.padmal@gmail.com"
	applicant.telephone="0710852311"
	applicant.gpa=3.9565
	applicant.aboutMe="I'm an Engineering undergraduate in university of Moratuwa"
	# Testing
	self.assertEquals(applicant.name, "Padmal")
	self.assertEquals(applicant.surname, "Knight")
	self.assertEquals(applicant.gender, "M")
	self.assertEquals(applicant.indexNumber, "140427D")
	self.assertEquals(applicant.email, "blog.padmal@gmail.com")
	self.assertEquals(applicant.telephone, "0710852311")
	self.assertEquals(applicant.gpa, 3.9565)
	self.assertEquals(applicant.aboutMe, "I'm an Engineering undergraduate in university of Moratuwa")

    def test_create_a_valid_preferences(self):
	# Creation
	prefs = Preferences()
	prefs.arduino = True
	prefs.wifi = True
	print prefs.get.wifi.display()
	# Testing
	self.assertEquals(prefs.iot, False)
	self.assertEquals(prefs.arduino, True)
	self.assertNotEquals(prefs.ai, True)

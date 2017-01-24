from django.conf.urls import url
from . import views

app_name = "companies"

urlpatterns = [
    url(r'^$', views.login, name='company-login'),
    url(r'^register/$', views.register, name='company-register'),
    url(r'^do_register/$', views.do_register, name='company-do-register'),
    url(r'^view/(?P<loginID>[A-Za-z0-9]+)/$', views.show, name='show'),
]

from django.conf.urls import url
from . import views

app_name = "users"

urlpatterns = [
    url(r'^$', views.login, name='user-login'),
    url(r'^register/$', views.register, name='user-register'),
    url(r'^do_register/$', views.do_register, name='user-do-register'),
    url(r'^view/(?P<index>[A-Za-z0-9]+)/$', views.show, name='show'),
]

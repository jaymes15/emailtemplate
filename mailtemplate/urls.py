from . import views
from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

 
app_name= 'mailtemplate'
urlpatterns = [
	path('', views.homepage,name='homepage'),
	path('sendmail/', views.sendmail,name='sendmail'),
	path("sendtemmail/", views.sendtemmail, name="sendtemmail")
	]
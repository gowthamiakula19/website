from django.conf.urls import url
from . import views

urlpatterns = [
         url(r'^$', views.home, name='home'),
         url(r'^contactus/$',views.contact, name='contactus'),
         url(r'^about/$', views.about, name='about'),

]

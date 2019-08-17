from django.conf.urls import url
from . import views #import views


# adding url
urlpatterns = [
    url('^$', views.index, name='home'), #home
    url(r'projects/', views.projects, name='projects'), #portfolio
    url(r'aboutme/',views.aboutme,name ='aboutme'),
    url(r'contact/', views.contact, name='contact'), #contact
]
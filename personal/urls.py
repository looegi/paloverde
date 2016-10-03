from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Register.html$', views.create, name='create'),
    url(r'^$', views.index, name='index')]

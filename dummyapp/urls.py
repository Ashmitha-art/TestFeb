from django.urls import path, re_path
from .views import *


app_name='someapp'

urlpatterns = [
    re_path('^$', someview, name='someview'),
    re_path('^delete/$', someviewNew, name='someviewNew'),
]

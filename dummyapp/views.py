from django.shortcuts import render
from .models import *

# Create your views here.


def someview(request):
    varName = newfunc()
    return render(request, 'sometemplate.html',{'randVar':varName})

def someviewNew(request):
    varNameNew = newfuncDelete()
    return render(request, 'sometemplate.html',{'randVarNew':varNameNew})

from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import HttpResponse
def index(request):
    tasks=Diary_model.objects.all()
    context={'tasks':tasks}

    return render(request,'index.html',context)
# lllllllllllllllllllllllll

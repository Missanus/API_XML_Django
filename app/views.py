from django.http import HttpResponse
from django.shortcuts import render
import requests






def homepage(request):
    return render(request, 'homepage.html')



# fuvntin get fire
def about(request):

    return render(request, 'about.html')

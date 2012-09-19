from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def homepage(request):
    current_date = datetime.datetime.now()
    return render_to_response('homepage/index.html', locals())

def current_datetime(request):
    current_date = datetime.datetime.now()
    return render_to_response('tests/current_datetime.html', locals())
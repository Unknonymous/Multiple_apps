# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#display a placeholder for all the surveys
def index(request):
    response = 'Placeholder to display all the surverys created'
    return HttpResponse(response)


#display a placeholder for users to add a new survey
def new(request):
    response = 'Placeholder for users to add a new survey'
    return HttpResponse(response)
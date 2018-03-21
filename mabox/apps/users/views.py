# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#display a placeholder for usesr to create a new user record

def register(reuqest):
    response ="Placeholder for  users to create a new user record"
    return HttpResponse (response)

def login(request):
    response = "Placeholder for users to login"
    return HttpResponse (response)

def new(request):
    return redirect ('/users/register')

def index(request):
    response = 'Placeholder to later display all the list of users'
    return HttpResponse(response)
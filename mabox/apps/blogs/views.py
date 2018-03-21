# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

#root route '/' handled by the blogs app
def root(request):
    response = "This is the root route. I am a sort of crossroads for the project.  I am being handled by the 'blogs' app."
    return HttpResponse(response)

# index lists all the blogs
def index(request):
    response = 'Placeholder to display all the list of blogs'
    return HttpResponse(response)

#form to create a new blog
def new(request):
    response = "Placeholder to display a new form to create a new blog"
    return HttpResponse(response)

#redirects to /blogs
def create(request):
    return redirect ('/blogs')

#placeholder to display blog by number handled by show()
def show(request,blog_id):
    response = "Placeholder to display blog {}".format(blog_id)
    return HttpResponse(response)

#placeholder to edit a blog by number
def edit(request, blog_id):
    response = "Placeholder to edit blog {}".format(blog_id)
    return HttpResponse(response)

#delete a blog by blog number, redirect to /blogs
def destroy(request, blog_id):
    return redirect("/blogs")
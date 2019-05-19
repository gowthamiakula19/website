# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,'learn/home.html')


def contact(request):
    return render(request,'learn/contactus.html')



def about(request):
    return render(request,'learn/about.html')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
import forms
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.template import loader, Context
from django.utils.crypto import get_random_string
from .models import Create
import os

# Call HTML Pages
@api_view(['GET'])
def formcreate(request,content=None):
    template = loader.get_template('register.html')
    if content:
        print(content)
        return render(request, 'register.html', content)
    else:
        return HttpResponse(template.render())


@api_view(['POST'])
def signup(request):
    import os
    print  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    form = forms.RegistForm(request.POST ,request.FILES)

    if form.is_valid():
        user = Create()
        user.EmailId = form.cleaned_data['EmailId']
        user.Address = form.cleaned_data['Address']
        user.EmpName = form.cleaned_data['EmpName']
        user.Password = form.cleaned_data['Password']
        user.Phone = form.cleaned_data['Phone']
        user.Image = form.cleaned_data['Image']
        user.AccessToken = get_random_string(length=32)
        user.save()
        template = loader.get_template('login.html')
        return HttpResponse(template.render())
    else:
        content = {'form': form}
        return render(request, 'register.html',content)


@api_view(['GET'])
def formlogin(request,content=None):
    template = loader.get_template('login.html')
    if content:
        print(content)
        return render(request, 'login.html', content)
    else:
        return HttpResponse(template.render())


@api_view(['GET','POST'])
def login(request):
    form = forms.Login(request.POST or None)
    if form.is_valid():

        emailId = form.cleaned_data['EmailId']
        password = form.cleaned_data['Password']
        try:
            userObjects = Create.objects.get(EmailId = emailId, Password = password)

            if userObjects:
                print "success"

                return render(request, 'user_details.html', {'list':userObjects})
            else:
                print "Fail"
        except Exception as e:
            print e

            return HttpResponse("Invalid Data")

    else:
        print request.data
        print(form.errors)
        content = {'form': form}
        return render(request, 'login.html', content)
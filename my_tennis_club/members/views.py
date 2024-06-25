from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def members_old(request):
    return HttpResponse("Hello world!")


def members(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def new_page(request):
    template = loader.get_template('new_page.html')
    return HttpResponse(template.render())

def stranka_b(request):
    template = loader.get_template('stranka_b.html')
    return HttpResponse(template.render())

def druha_stranka(request):
    template = loader.get_template('druha_stranka.html')
    return HttpResponse(template.render())

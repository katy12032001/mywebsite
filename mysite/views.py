# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response, render

def here(request):
    return HttpResponse('Mom, I am here!我 ')

def add(request, a, b):
    s = int(a) + int(b)
    value = {'s': s}
    # t = get_template('math.html')
    # c = template.Context({'s': s})
    # return HttpResponse(t.render(c))
    return render_to_response('math.html', locals())
    # return render(request, 'math.html', {
    #     's': s})

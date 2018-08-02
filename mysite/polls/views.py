# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,Http404
from django.template import loader
from .models import Question


def index(request):
    latest_ques_list= Question.objects.order_by('-pub_date')[:5]
    # output=','.join([q.question_text for q in latest_ques_list])
   # template=loader.get_template('polls/index.html')
    context ={
       'latest_ques_list' : latest_ques_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("No question found")
    return  render(request,'polls/detail.html',{'question':question})
    # return HttpResponse('Hi')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


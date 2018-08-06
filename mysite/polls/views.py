# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from .models import Question
from django.urls import reverse
from django.views import generic


# def index(request):
#     latest_ques_list= Question.objects.order_by('-pub_date')[:5]
#     # output=','.join([q.question_text for q in latest_ques_list])
#    # template=loader.get_template('polls/index.html')
#     context ={
#        'latest_ques_list' : latest_ques_list,
#     }
#     # return HttpResponse(template.render(context,request))
#     return render(request,'polls/index.html',context)

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_ques_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request,question_id):
#     try:
#         question=Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("No question found")
#     return  render(request,'polls/detail.html',{'question':question})

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

# def results(request, question_id):
#     question=get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})

class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question

def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    print question
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
        print selected_choice
    except:
        return render(request, 'polls/detail.html',{'question': question, 'error_message': 'You did not select a choice'})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))



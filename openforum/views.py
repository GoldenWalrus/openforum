from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openforum.models import User, Question, Response

def index(request):
    # worry about authenticating user later
    question_list = Question.objects.order_by('-date')[:5]
    return render(request, 'index.html', {'question_list' : question_list })

def detail(request):
    return HttpResponse('You are looking at a post in detail')

def respond(request):
    # create a new Response
    return HttpResponse('You are responding to a question')

def ask(request):
    # create a new post
    return HttpResponse('You are asking a question')

def logout(request):
    request.session['username'] = ''
    return HttpResponseRedirect('/portal/') # portal will be handled in a separate app

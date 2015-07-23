from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openforum.models import User, Question, Response, Board

def index(request):
    # get a list of all boards
    board_list = Board.objects.all()
    return render(request, 'index.html', {'board_list', board_list})

def board(request):
    # worry about authenticating user later
    # get the board name
    return render(request, 'board.html', {'question_list' : question_list, 'board_name' : board_name })

def question(request):
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

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openforum.models import User, Question, Response, Board
import hashlib, smtplib # hash and mail functions

def index(request):
    # get a list of all boards
    board_list = Board.objects.all()[:5] # only first 5
    return render(request, 'index.html', {'board_list' : board_list})

def board(request, boardname):
    # worry about authenticating user later
    # get the board name
    try:
        board_name = boardname
        question_list = Question.objects.filter(board__name = boardname) # point to the board
        return render(request, 'board.html', {'question_list' : question_list, 'board_name' : board_name })
    except Board.DoesNotExist:
        raise Http404("Board does not exist")

def question(request, boardname, questionid):
    try:
        q = Question.objects.get(questionnumber = questionid, board__name = boardname)
        text = q.questiontext
        response_list = Response.objects.filter(question__questionnumber = questionid)
        return render(request, 'question.html', {'response_list' : response_list, 'text' : text, 'boardname' : boardname })
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # USE RENDER TO PASS CONTEXT IF THERE IS AN ERRROR! DONT REDIRECT

def login(request):
    try:
        result = User.objects.get(name=request.POST['username'], password=hashlib.sha224(request.POST['password']).hexdigest())
        request.session['username'] = request.POST['username']
        return HttpResponseRedirect('/openforum/')
    except User.DoesNotExist:
        return render(request, 'index.html', {'error_message' : 'Your username and password combination was incorrect'})

def register(request):
    return render(request, 'register.html')

def makeaccount(request):
    try:
        newuser = User(name=request.POST['username'], password=request.POST['password'], email=request.POST['email'], verification_code=hashlib.md5(request.POST['username']).hexdigest())
        newuser.save()
        return HttpResponseRedirect('/openforum/')
    except KeyError:
        return render(request, 'index.html', {'error_message' : 'There was an error registering your account. Please try again.'})

def respond(request):
    # create a new Response
    return HttpResponse('You are responding to a question')

def ask(request):
    # create a new post
    return HttpResponse('You are asking a question')

def logout(request):
    request.session['username'] = ''
    return HttpResponseRedirect('/portal/') # portal will be handled in a separate app

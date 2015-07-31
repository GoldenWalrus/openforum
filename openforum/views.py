from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from openforum.models import User, Question, Response, Board
import hashlib, smtplib # hash and mail functions

def getTheme(r): # r is the request
    try:
        u = User.objects.get(name=r.session['username'])
        return u.theme
    except User.DoesNotExist:
        return "default"

def index(request):
    # get a list of all boards
    board_list = Board.objects.all()[:5] # only first 5
    return render(request, 'index.html', {'board_list' : board_list , 'theme' : 'default'})

def board(request, boardname):
    # worry about authenticating user later
    # get the board name
    try:
        board_name = boardname
        question_list = Question.objects.filter(board__name = boardname) # point to the board
        return render(request, 'board.html', {'question_list' : question_list, 'board_name' : board_name , 'theme' : 'default' })
    except Board.DoesNotExist:
        raise Http404("Board does not exist")

def question(request, boardname, questionid):
    try:
        q = Question.objects.get(pk = questionid, board__name = boardname)
        text = q.questiontext
        response_list = Response.objects.filter(question__pk = questionid)
        return render(request, 'question.html', {'response_list' : response_list, 'text' : text, 'boardname' : boardname, 'theme' : 'default' })
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # USE RENDER TO PASS CONTEXT IF THERE IS AN ERRROR! DONT REDIRECT

def login(request):
    try:
        result = User.objects.get(name=request.POST['username'], password=hashlib.sha224(request.POST['password']).hexdigest())
        request.session['username'] = request.POST['username']
        return HttpResponseRedirect('/openforum/')
    except User.DoesNotExist:
        return render(request, 'index.html', {'error_message' : 'Your username and password combination was incorrect' , 'theme' : 'default' })

def register(request):
    return render(request, 'register.html')

def makeaccount(request):
    try:
        newuser = User(name=request.POST['username'], password=hashlib.sha224(request.POST['password1']).hexdigest(), email=request.POST['email'], verification_code=hashlib.md5(request.POST['username']).hexdigest(), theme='default')
        newuser.save()
        return HttpResponseRedirect('/openforum/')
    except KeyError:
        return render(request, 'index.html', {'error_message' : 'There was an error registering your account. Please try again.', 'theme' : 'default'})

def respond(request):
    # create a new Response
    try:
        return 0
        #newresponse = Response(question='fasdfdasf' ,responsetext=)
    except:
        return HttpResponse('YOU FAIL!')

def ask(request):
    # create a new post
    try:
        newquestion = Question(questiontext=request.POST['questiontext'], date=timezone.now(), author=request.session['username'], board='13041304')
        newquestion.save()
    except:
        return render(request, 'index.html', {'error_message' : 'There was an error creating your post. Sorry about that.', 'theme' : 'default'})

def logout(request):
    request.session['username'] = ''
    return HttpResponseRedirect('/portal/')

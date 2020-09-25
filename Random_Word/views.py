from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    
    request.session['random_word'] = get_random_string(length=14)
    return render(request, 'random_word.html')

def generate(request):
    request.session['random_word'] = get_random_string(length=14)
    request.session['counter'] += 1
    return redirect('/random_word')
def reset(request):
    request.session['counter'] = 1
    return redirect('/random_word')
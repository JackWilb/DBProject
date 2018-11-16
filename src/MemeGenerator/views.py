from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'MemeGenerator/index.html')

def login(request):
	return render(request, 'MemeGenerator/login.html')

def makeameme(request):
	return render(request, 'MemeGenerator/makeameme.html')

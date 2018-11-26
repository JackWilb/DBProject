from django.shortcuts import render
from django.http import HttpResponse
from MemeGenerator.models import Template

def index(request):
	# Get 2 memes from our database
	meme1 = Template.objects.get(id=1)
	meme2 = Template.objects.get(id=2)

	context = {
		'leftMeme': meme1,
		'rightMeme': meme2
	}
	return render(request, 'MemeGenerator/index.html', context)

def login(request):
	return render(request, 'MemeGenerator/login.html')

def makeameme(request):
	return render(request, 'MemeGenerator/makeameme.html')

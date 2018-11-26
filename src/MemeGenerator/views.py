from django.shortcuts import render, redirect
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
	if request.method == 'POST':
		# Get the data
		data = request.REQUEST
		# Build the meme and save
		print(data)
		# Input data into database

		# Redirect off the page so we know it worked
		return redirect('/static/MemeGenerator/styles.css')
	else:
		# If not post then go to the page so we can make a post
		return render(request, 'MemeGenerator/makeameme.html')

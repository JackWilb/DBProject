from django.shortcuts import render, redirect
from django.http import HttpResponse
from MemeGenerator.models import Template, Meme, Text

import os
import math
import random

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
		memeTemplate = request.POST.get('memeTemplate')
		topText = request.POST.get('topText')
		bottomText = request.POST.get('bottomText')

		# Build the meme and save
		# See which memeTemplate
		if (memeTemplate == '1'):
			meme_id = 1
		elif (memeTemplate == '2'):
			meme_id = 3
		else:
			meme_id = 2
		template = Template.objects.get(id=meme_id)
		random_file_number = math.floor(random.random() * 4294967295)

		file_path_root = "~/websites/DBProject/src/MemeGenerator/"
		command1 = "width=`identify -format %w " + file_path_root + str(template.image) +  "`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:'" + str(topText) + "' rickAstley.jpg +swap -gravity south -composite " + file_path_root + "media/MemegGenerator/temp.jpg"
		command2 = "width=`identify -format %w " + file_path_root + "media/MemegGenerator/temp.jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:'" + str(topText) + "' rickAstley.jpg +swap -gravity south -composite  " + file_path_root + "media/MemegGenerator/temp.jpg"
		os.system(command1)
		os.system(command2)

		# Input data into database
		# Input text into DB
		new_row_text = Text(top = topText, bottom = bottomText)
		new_row_text.save();

		# Construct a new meme and save it to the database
		new_row_meme = Meme(
			templateid = Template.objects.get(id=meme_id), 
			textid = Text.objects.get(top = topText), 
			image = "/media/MemegGenerator/temp.jpg", 
			userid = None
		)
		new_row_meme.save()
		# Redirect off the page so we know it worked
		return redirect('/index.html')
	else:
		# If not post then go to the page so we can make a post
		return render(request, 'MemeGenerator/makeameme.html')

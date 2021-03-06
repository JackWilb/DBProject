from django.shortcuts import render, redirect
from django.http import HttpResponse
from MemeGenerator.models import Template, Meme, Text, Tag, Memetag, User, Taguser, Comment, Likereaction

import os
import math
import random

def index(request):
	if request.method == 'POST':
		comment = request.POST.get('comment')
		user = request.COOKIES.get('username')
		meme = request.POST.get('meme')

		if user == None:
			user = 'Anonymous'

		new_row_Comment = Comment(
			userid = User.objects.get(login = user),
			memeid = Meme.objects.get(id = int(float(meme))),
			comment = comment
			)
		new_row_Comment.save()

		return redirect('/')

	elif request.GET.getlist('tags'):
		# Get Query tags
		tags = request.GET.getlist('tags')

		# Check if we have a meme with those tags if not redirect to index
		if Meme.objects.values('memetag', 'image').filter(memetag__tagid__in=tags).count() == 0:
			return redirect('/')

		# Get 2 random indicies
		randomindex1 = random.randint(0, Meme.objects.filter(memetag__tagid__in=tags).count() - 1)
		randomindex2 = random.randint(0, Meme.objects.filter(memetag__tagid__in=tags).count() - 1)

		if (randomindex1 == randomindex2):
			randomindex2 = random.randint(0, Meme.objects.filter(memetag__tagid__in=tags).count() - 1)

		# Get Memes based on random indicies
		meme1 = Meme.objects.filter(memetag__tagid__in=tags)[randomindex1]
		meme2 = Meme.objects.filter(memetag__tagid__in=tags)[randomindex2]

		# Get Comments for those memes
		leftComments = Comment.objects.filter(memeid = meme1.id)
		rightComments = Comment.objects.filter(memeid = meme2.id)

		# Get authors for the comments
		leftAuthors = []
		rightAuthors = []

		for i in range(len(leftComments.values())):
			tuple = (User.objects.get(id=leftComments.values()[i].get('userid_id')), leftComments[i])
			leftAuthors.append(tuple)

		for i in range(len(rightComments.values())):
			tuple = (User.objects.get(id=rightComments.values()[i].get('userid_id')), rightComments[i])
			rightAuthors.append(tuple)

		# Get likes for those memes
		leftLikes = None
		rightLikes = None

		# Get tags for filtering
		allTags = Tag.objects.all()

		context = {
			'leftMeme': meme1,
			'rightMeme': meme2,
			'leftComments': leftComments,
			'rightComments': rightComments,
			'leftAuthors': leftAuthors,
			'leftRange': range(len(leftAuthors)),
			'rightRange': range(len(rightAuthors)),
			'rightAuthors': rightAuthors,
			'leftLikes': leftLikes,
			'rightLikes': rightLikes,
			'allTags': allTags
		}
		return render(request, 'MemeGenerator/index.html', context)
	else:
		# Get 2 random indicies
		randomindex1 = random.randint(0, Meme.objects.count() - 1)
		randomindex2 = random.randint(0, Meme.objects.count() - 1)

		if (randomindex1 == randomindex2):
			randomindex2 = random.randint(0, Meme.objects.count() - 1)

		# Get Memes based on random indicies
		meme1 = Meme.objects.all()[randomindex1]
		meme2 = Meme.objects.all()[randomindex2]

		# Get Comments for those memes
		leftComments = Comment.objects.filter(memeid = meme1.id)
		rightComments = Comment.objects.filter(memeid = meme2.id)

		# Get authors for the comments
		leftAuthors = []
		rightAuthors = []

		for i in range(len(leftComments.values())):
			tuple = (User.objects.get(id=leftComments.values()[i].get('userid_id')), leftComments[i])
			leftAuthors.append(tuple)

		for i in range(len(rightComments.values())):
			tuple = (User.objects.get(id=rightComments.values()[i].get('userid_id')), rightComments[i])
			rightAuthors.append(tuple)

		# Get likes for those memes
		leftLikes = None
		rightLikes = None

		# Get tags for filtering
		allTags = Tag.objects.all()

		context = {
			'leftMeme': meme1,
			'rightMeme': meme2,
			'leftComments': leftComments,
			'rightComments': rightComments,
			'leftAuthors': leftAuthors,
			'rightAuthors': rightAuthors,
			'leftRange': range(len(leftAuthors)),
			'rightRange': range(len(rightAuthors)),
			'leftLikes': leftLikes,
			'rightLikes': rightLikes,
			'allTags': allTags
		}
		return render(request, 'MemeGenerator/index.html', context)

def login(request):
	if request.method == 'GET' and request.GET.get('accountName') != None:
		# Set cookie attributes
		accountName = request.GET.get('accountName')
		max_age = 7*24*60*60

		# Check if user exists, if not render makeanaccount
		if User.objects.filter(login = accountName).count() == 0:
			return redirect('/makeanaccount/')
		else:
			# Make page and attach cookie
			response = redirect('/')
			response.set_cookie('username', value = accountName, max_age = max_age)
			return response
	else:
		return render(request, 'MemeGenerator/login.html')

def makeatag(request):
	if request.method == 'POST':
		tag = request.POST.get('tag')
		user = request.COOKIES.get('username')

		if not Tag.objects.filter(name = tag).exists() and tag.strip():
			new_row_Tag = Tag(name = tag)
			new_row_Tag.save()
			new_row_Taguser = Taguser(userid = User.objects.get(login = user), 
				tagid = new_row_Tag)
			new_row_Taguser.save()

		return redirect('/makeameme/')

	else:
		return render(request, 'MemeGenerator/makeatag.html')

def makeameme(request):
	if request.method == 'POST':
		# Get the data
		memeTemplate = request.POST.get('memeTemplate')
		topText = request.POST.get('topText')
		bottomText = request.POST.get('bottomText')
		tags = request.POST.getlist('tags')
		user = request.COOKIES.get('username')

		template = Template.objects.get(id=memeTemplate)
		random_file_number = math.floor(random.random() * 4294967295)

		file_path_root = "~/websites/DBProject/src/"
		command1 = "width=`identify -format %w " + file_path_root + str(template.image) + "`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:'" + str(topText) + "' " + file_path_root + str(template.image) + " +swap -gravity north -composite " + file_path_root + "media/MemeGenerator/temp" + str(random_file_number) +".jpg"
		command2 = "width=`identify -format %w " + file_path_root + "media/MemeGenerator/temp" + str(random_file_number) +".jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:'" + str(bottomText) + "' " + file_path_root + "media/MemeGenerator/temp" + str(random_file_number) +".jpg +swap -gravity south -composite  " + file_path_root + "media/MemeGenerator/" + str(random_file_number) + ".jpg"
		os.system(command1)
		os.system(command2)

		# Input data into database
		# Input text into DB
		new_row_text = Text(top = topText, bottom = bottomText)
		new_row_text.save();

		user = request.COOKIES.get('username')

		if user != None:
			user = User.objects.get(login = user)
		else:
			user = User.objects.get(login = 'Anonymous')

		# Construct a new meme and save it to the database
		new_row_meme = Meme(
			templateid = template, 
			textid = Text.objects.get(top = topText), 
			image = "/media/MemeGenerator/" + str(random_file_number) + ".jpg", 
			userid = user
		)
		new_row_meme.save()

		# Input Tags
		for tag in tags:
			new_row_Memetag = Memetag(
				memeid = new_row_meme,
				tagid = Tag.objects.get(id=tag)
			)
			new_row_Memetag.save()

		# Redirect off the page so we know it worked
		return redirect('/')
	else:
		# If not post then go to the page so we can make a post

		# Get Tags to pass into context
		tags = Tag.objects.all()

		# Get all Templates to pass to context
		templates = Template.objects.all()

		# Set context
		context = {'tags': tags, 'templates': templates}

		return render(request, 'MemeGenerator/makeameme.html', context)

def makeanaccount(request):
	if request.method == 'POST':
		user = request.POST.get('user')

		if user.strip():
			if User.objects.filter(login = user).count() == 0 and user != None:
				new_row_User = User(login = user)
				new_row_User.save()

		return redirect('/login/')

	else:
		return render(request, 'MemeGenerator/makeanaccount.html')

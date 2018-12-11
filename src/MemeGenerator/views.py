from django.shortcuts import render, redirect
from django.http import HttpResponse
from MemeGenerator.models import Template, Meme, Text, Tag, Memetag, User, Taguser, Comment, Likereaction

import os
import math
import random

def index(request):
	if request.method == 'POST':
		pass
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
			randomindex2 = random.randint(0, Meme.objects.values('memetag', 'image').filter(memetag__tagid__in=tags).count() - 1)

		# Get Memes based on random indicies
		meme1 = Meme.objects.filter(memetag__tagid__in=tags)[randomindex1]
		meme2 = Meme.objects.filter(memetag__tagid__in=tags)[randomindex2]

		# Get Comments for those memes
		leftComments = Comment.objects.filter(memeid = meme1.id)
		rightComments = Comment.objects.filter(memeid = meme2.id)

		# Get authors for the comments
		leftAuthors = []
		rightAuthors = []

		#for a in leftComments.values('id'):
		#	leftAuthors.append(User.objects.filter(id=a.get('id')))

		#for a in rightComments.values('id'):
		#	rightAuthors.append(a.get('id'))

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

		for a in leftComments.values('id'):
			leftAuthors.append(a.get('id'))

		for a in rightComments.values('id'):
			rightAuthors.append(a.get('id'))

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

		file_path_root = "~/websites/DBProject/src/"
		command1 = "width=`identify -format %w " + file_path_root + str(template.image) + "`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:'" + str(topText) + "' " + file_path_root + str(template.image) + " +swap -gravity north -composite " + file_path_root + "media/MemeGenerator/temp" + str(random_file_number) +".jpg"
		command2 = "width=`identify -format %w " + file_path_root + "media/MemeGenerator/temp" + str(random_file_number) +".jpg`;   convert -background '#0008' -fill white -font Impact -gravity center -size ${width}x30 caption:'" + str(bottomText) + "' " + file_path_root + "media/MemeGenerator/temp" + str(random_file_number) +".jpg +swap -gravity south -composite  " + file_path_root + "media/MemeGenerator/" + str(random_file_number) + ".jpg"
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
			image = "/media/MemeGenerator/" + str(random_file_number) + ".jpg", 
			userid = None
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

		# Set context
		context = {'tags': tags}

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

from django.shortcuts import render, redirect
from django.http import HttpResponse
from MemeGenerator.models import Template, Meme, Text

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
		print()
		file_path = 1
		# Input data into database
		# Input text into DB
		new_row_text = Text(top = topText, bottom = bottomText)
		new_row_text.save();

		# See which memeTemplate
		if (memeTemplate == '1'):
			meme_id = 1
		elif (memeTemplate == '2'):
			meme_id = 3
		else:
			meme_id = 2

		new_row_meme = Meme(templateid = meme_id, textid = Text.objects.get(top = topText).id[0], image = file_path, userid = None)
		# Redirect off the page so we know it worked
		return redirect('/static/MemeGenerator/styles.css')
	else:
		# If not post then go to the page so we can make a post
		return render(request, 'MemeGenerator/makeameme.html')

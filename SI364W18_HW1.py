## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".

##phill brown
##used stackoverflow

import requests
import json

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/class')
def welcome():
	return 'Welcome to SI 364!'

@app.route('/movie/<movie_name>')  ##gets movie information from itunes api and presents it in very ugly text format
def movie_find(movie_name):
	baseurl ='https://itunes.apple.com/search?'
	param_dict = {'term': movie_name, 'entity': 'movie'}
	movie_info = requests.get(baseurl, params = param_dict)

	return(movie_info.text)

@app.route('/question')
def number_question():
	nub_ques = """<!DOCTYPE html>
	<html>
	<body>
	<form action = "/result" method ="POST">
		<p>Enter a number pls</p>
		<input type = "text" name ="num" value="Enter your favorite number">
		<br>
		<input type = "submit" value = "Click to Submit">
	</form>
	</break>
	</html>"""

	return nub_ques


@app.route('/result', methods =['POST', 'GET'])
def num_result():
	if request.method =='POST':
		number = request.form['num']
	s = 'Double your favorite number is {}'.format(int(number)*2)

	return s

@app.route('/problem4form', methods = ['POST', 'GET'])
def problem4():
	d = """<!DOCTYPE html>
	<html>
	<body>
	<form action = '/problem4form' method = 'POST'>
		<input type = 'text' name = 'artist' value = 'musician'>
		<br>
		<p>What would you like?</p>
		<p>5 songs</p>
			<input type = 'checkbox' name = 'songs' value = 'songs'>
		<p>5 albums</p>
			<input type = 'checkbox' name = 'albums' value = 'albums'>
		<br>
		<input type = 'submit' value = 'click to submit'>
		
	</form
	</body>
	</html>"""

	final_dic= {}
	if request.method == 'POST':
		artist_name = request.form['artist']

		baseurl = 'https://itunes.apple.com/search?'
		param_dict = {'term': artist_name, 'entity': 'musicArtist'}
		artist_info = requests.get(baseurl, params = param_dict)

		artist_info = artist_info.json()
		
		names = []

		for each in artist_info['results']:
			names.append(each['artistName'])
		
		if request.form.get('songs'):
			param_dict = {'term': artist_name, 'entity': 'song'}
			song_list = requests.get(baseurl, params = param_dict)
			song_list = song_list.json()

			thesongs = []
			for each in song_list['results'][0:5]:
				thesongs.append(each['trackCensoredName'])
			final_dic['Songs'] = thesongs

		if request.form.get('albums'):
			param_dict = {'term': artist_name, 'entity': 'album'}
			albums = requests.get(baseurl, params = param_dict)
			albums = albums.json()

			thealbums = []
			for each in albums['results'][0:5]:
				thealbums.append(each['collectionName'])
			final_dic['Albums'] = thealbums 

		return d + str(final_dic)


	else:

		return d



	

	




if __name__ == '__main__':
    app.run()




## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.

import webbrowser

class Movie(object):
	''' This class provides a way to store movie related information '''
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		# This is the movie title
		self.title = movie_title
		
		# This is the storyline of the movie
		self.storyline = movie_storyline
		
		# A link to the poster
		self.poster_image_url = poster_image
		
		# A link to trailer
		self.trailer_youtube_url = trailer_youtube
	
	
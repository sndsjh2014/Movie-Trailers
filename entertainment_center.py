import fresh_tomatoes
import media

# Define several instances of the Movie class
toy_story = media.Movie("Toy Story", "A story of a boy and his toys",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")
	
skyfall = media.Movie("Sky Fall", "23 James Bond film",
	"https://upload.wikimedia.org/wikipedia/en/a/a7/Skyfall_poster.jpg",
	"https://www.youtube.com/watch?v=6kw1UVovByw")
	
forest_gump = media.Movie("Forest Gump", "A disadvantaged boy never thought of himself as such",
	"https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
	"https://www.youtube.com/watch?v=eYSnxZKTZzU")
	
gladiator = media.Movie("Gladiator", "Commodus relegates Maximus to fight to the death in the gladiator arenas.",
	"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
	"https://www.youtube.com/watch?v=W1rNFuKFTnc")
	
frozen = media.Movie("Frozen", "Story",
	"https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
	"https://www.youtube.com/watch?v=TbQm5doF_Uc")

# List of movies
movies = [skyfall, forest_gump, gladiator, frozen, toy_story, avatar]

# Pass movies list to open_movies_page function
fresh_tomatoes.open_movies_page(movies)

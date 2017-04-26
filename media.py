import webbrowser

class Movie():
    """Class defining a movie.
    
    The Movie class contains various pieces of data pertaining to a specific
    movie. This data includes the movie title, brief description, the location
    of the movie's poster image, and the location of the movie's trailer on
    youtube. This class also has a method for opening the browser and playing
    the movie's trailer.
    
    Attributes:
        title: A string of the movie title.
        storyline: A string quickly describing the premis of the movie.
        poster_image_url: A string of the url to a poster image for the movie.
        trailer_youtub_url: A string of the url to the youtube trailer of the
            movie.
    """
    
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Inits Movie.
        
        Initializes Movie object.
                
        Args:
            title: A string of the movie title.
            storyline: A string quickly describing the premis of the movie.
            poster_image_url: A string of the url to a poster image for the
                movie.
            trailer_youtub_url: A string of the url to the youtube trailer of
                the movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """Plays movie trailer in browser.
        
        Opens the webbrowser and playes the movie found at
        self.trailer_youtube_url
        
        Args:
            None
        """
        webbrowser.open(self.trailer_youtube_url)

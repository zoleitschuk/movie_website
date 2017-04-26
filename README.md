# Me Through Movies
***
Me Through Movies is an archive of my favorite movie during each year of my life. This folder contains an html document where you can view the movie poster and the associated trailer for each of my favorite movies. The folder also contains the python code used to generate this html file in case you are feeling nostalgic and want to build your own version of Me Through Movies.
## Quickstart
***
### View
To view Me Through Movies simply open the [me_through_movies.html](./me_through_movies.html) in the webbrowser of your choice.
### Modify
If you would like to change the movies within Me Through Movies, open [entertainment_center.py](entertainment_center.py) in the text editor of you choice. Within [entertainment_center.py](entertainment_center.py) you will see many different movie definitions that look similar to:
```python
FANTASIA = media.Movie('Fantasia',
        'A timeless Disney motion picture, set to classical music.',
        'https://upload.wikimedia.org/wikipedia/en/1/12/Fantasia-poster-1940.jpg',
        'https://www.youtube.com/watch?v=LpKA9n-75tQ')
```
You can define your own movies by copying this format, and adding them to [entertainment_center.py](entertainment_center.py).
>Note for more information on defining your own movies see the documentation inside [media.py](./media.py)

Once you have defined all the movies you want to add, go to the bottom of [entertainment_center.py](entertainment_center.py) where you will find a list of movies, such as:
```python
MOVIES = [
            THE_LAND_BEFORE_TIME,
            ROBIN_HOOD,
            THE_SWORD_IN_THE_STONE,
            FANTASIA,
            THE_SECRET_OF_NIHM,
            ROCK_A_DOODLE,
            FERN_GULLY,
            THE_NIGHTMARE_BEFORE_CHRISTMAS
            ]
```
Replace and re-order items within this list to have the changes you made reflected when you rebuild [me_through_movies.html](./me_through_movies.html).
>Note: List order in MOVIES matters. The order within the list is assumed to be the age at which the movies was your favorite movie. For example, in the above MOVIES list THE_LAND_BEFORE_TIME will be labeled with "Age 0" when [me_through_movies.html](./me_through_movies.html) is opened,  ROBIN_HOOD with "Age 1", THE_SWORD_IN_THE_STONE with "Age 2", and so on..
### Build
Once you have finished modifying entertainment_center.py you will want to rebuild me_through_movies.html to reflect your changes. To do this simply run `python entertainment_center.py` in the command line. Once this command has been run [me_through_movies.html](./me_through_movies.html) will reflect all changes made within
>Note: You will need either python 2.X or 3.X installed in order to use the python command.

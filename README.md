python-allocine
===============

Allocine is a website (www.allocine.fr) that contains lot of information about movies, actors, directors, users rating, etc.

The python-allocine library allows to search movies and persons on the Allocine's website using their API. The results are in JSON format.

For now, we can search movies (including user rating, press rating, images, title, casting, release date, link), persons (picture, name, birthday date, nationality, real name, list of activity), get filmography of a person.

File Edit Options Buffers Tools Python Help



example.py
==========
```
#!/usr/bin/env python                                                                                                                                                                                                                       

from allocine.Allocine import *

if __name__ == "__main__":

    movies = search_movie("the godfather")
    movie = movies[0]

    print "Titre:", movie.title
    print "Annee:", movie.productionYear
    print "Note internautes:", movie.userRating, "/ 5.0"
    print "Acteurs:", movie.actors
```

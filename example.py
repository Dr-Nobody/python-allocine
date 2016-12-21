#!/usr/bin/env python

from allocine.Allocine import *



if __name__ == "__main__":
    
    
    movies = search_movie("the godfather")
    movie = movies[0]
    
    print "Titre:", movie.title
    print "Annee:", movie.productionYear
    print "Note internautes:", movie.userRating, "/ 5.0"
    print "Acteurs:", movie.actors
        
    #print(movie.synopsisShort)

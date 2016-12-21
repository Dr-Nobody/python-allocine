# -*- coding: latin-1 -*-
import urllib, urllib2, json
from settings import *
from Movie import Movie
from Person import Person
from Review import Review
import requests, time, hashlib, sys, base64
from datetime import date


def search_movie(qry, count=1):
    headers = {"User-Agent":"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Nexus 4 Build/JDQ39E)"}
    url = "http://api.allocine.fr/rest/v3/search"
    
    qry = qry.encode("latin1").replace("\xe9", "e").replace("\xe8", "e").replace("\xe7", "c").replace("\xea", "a")
    
    try:
        sed = str(date.today().strftime("%Y%m%d"))
        sig = hashlib.sha1(SECRET_KEY + "partner="+PARTNER_CODE+"&q="+qry.replace(" ","+")+"&format=json&filter=movie&count=" + str(count) + '&sed=' + sed).digest().encode("base64").replace("\n","").replace("+", "%2B").replace("=", "%3D").replace("/", "%2F")
        url += '?' + "partner="+PARTNER_CODE+"&q="+qry.replace(" ","+") + "&format=json&filter=movie&count=" + str(count) + '&sed=' + sed + '&sig=' + sig
        
    except UnicodeEncodeError:
        return []
    
    e = requests.get(url, headers=headers).text
    
    d = json.loads(e)
    feed = d["feed"]
    
    movies = []
    
    if feed["totalResults"] > 0:
      if "movie" in feed:
        for movie in feed["movie"]:
          m = Movie(movie)
          
          movies.append(m)
    else:
      movies = []
    return movies
  

def search_person(qry, count=1):
    headers = {"User-Agent":"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Nexus 4 Build/JDQ39E)"}
    url = "http://api.allocine.fr/rest/v3/search"
    sed = str(date.today().strftime("%Y%m%d"))
    sig = hashlib.sha1(SECRET_KEY + "partner="+PARTNER_CODE+"&q="+qry.replace(" ","+")+"&format=json&filter=person&count=" + str(count) + '&sed=' + sed).digest().encode("base64").replace("\n","").replace("+", "%2B").replace("=", "%3D").replace("/", "%2F")
    url += '?' + "partner="+PARTNER_CODE+"&q="+qry.replace(" ","+") + "&format=json&filter=person&count=" + str(count) + '&sed=' + sed + '&sig=' + sig
    
    e = requests.get(url, headers=headers).text
    d = json.loads(e)
    
    feed = d["feed"]
    
    persons = []
    
    if feed["count"] > 0:
      if "person" in feed:
        for person in feed["person"]:
          p = Person(person)
          
          persons.append(p)
    else:
      persons = []
    return persons

  
#def getMovie(code, profile = DEFAULT_PROFILE):
#    retval = Movie(code = code)
#    retval.getInfo(profile)
#    return retval

#def getPerson(code, profile = DEFAULT_PROFILE):
#    retval = Person(code = code)
#    retval.getInfo(profile)
#    return retval

#def reviewList(movie_code):
#    url = "http://api.allocine.fr/rest/v3/search"
#    sed = str(date.today().strftime("%Y%m%d"))
#    sig = hashlib.sha1(SECRET_KEY + "partner="+PARTNER_CODE+"&q="+qry.replace(" ","+")+"&format=json&filter=movie&count=" + str(count) + '&sed=' + sed).digest().encode("base64").replace("\n","").replace("+", "%2B").replace("=", "%3D")
#    url += '?' + "partner="+PARTNER_CODE+"&q="+qry.replace(" ","+") + "&format=json&filter=movie&count=" + str(count) + '&sed=' + sed + '&sig=' + sig
#    e = requests.get(url, headers=self.headers).text
#    return [Review(**i) for i in d["feed"]["review"]]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    print "Searching...", sys.argv[1]

    
    person = search_person(sys.argv[1])
    for m in person:
      print m.name, m.gender, m.birthDate, m.nationality, m.realName, m.activity
      for a in m.getFilmography():
        print a["title"], a["productionYear"], a["role"], a["activity"]
      break
    
    sys.exit(0)
    
    movies = search_movie(sys.argv[1])
    
    for m in movies:
      print m.title, m.release, m.productionYear, m.directors, m.userRating
    
    sys.exit(0)
    
    print "-------------"
    
  
  p.getFilmography()
  for m in p.filmography:
    print("%s played in %s" % (p, m.movie))
  m = Movie(code=  32070)
  #m.getInfo(profile = "large")

  print("searching 'le parrain'")
  results = Allocine().search("the godfather")
  movie = results.movies[0]
  print("first result is %s" % movie)
  #movie.getInfo()
  print("synopsis of %s : %s" % (movie, movie.synopsisShort))

from AllocineObject import *
import Movie
import requests, base64, hashlib, json
from datetime import date
from settings import *


class Person:
  
#  class Participation(object):
#    def __init__(self, activity, movie):
#      self.activity = activity
#      self.movie = movie

  def __init__(self, code):
    self.code = code["code"]
    #print code
    
    if "picture" in code:
      self.picture = code["picture"]["href"]
    else:
      self.picture = "<unknown>"

    if "name" in code:
      self.name = code["name"]
    else:
      self.name = "<unknown>"

    if "gender" in code:
      if code["gender"] == 2:
        self.gender = "woman"
      else:
        self.gender = "man"
    else:
      self.gender = "<unknown>"

    if "birthDate" in code:
      d = datetime.strptime(code["birthDate"], '%Y-%m-%d')
      self.birthDate = d.strftime('%d/%m/%Y')
    else:
      self.birthDate = "<unknown>"

    if "nationality" in code:
      self.nationality = code["nationality"][0]["$"]
    else:
      self.nationality = "<unknown>"

    if "realName" in code:
      self.realName = code["realName"]
    else:
      self.realName = "<unknown>"

    if "link" in code:
      self.link = code["link"][0]["href"]
    else:
      self.link = "<unknown>"
      
    if "activity" in code:
      self.activity = []
      for a in code["activity"]:
        self.activity.append(a["$"])
    else:
      self.activity = []

      
  def __unicode__(self):
    return self.realName


  def getFilmography(self, profile = DEFAULT_PROFILE):
    
    qry = str(self.code)
    count = "1"
    
    headers = {"User-Agent":"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Nexus 4 Build/JDQ39E)"}
    url = "http://api.allocine.fr/rest/v3/filmography"
    sed = str(date.today().strftime("%Y%m%d"))
    sig = hashlib.sha1(SECRET_KEY + "partner="+PARTNER_CODE+"&code="+qry.replace(" ","+")+"&format=json&filter=person&count=" + str(count) + '&sed=' + sed).digest().encode("base64").replace("\n","").replace("+", "%2B").replace("=", "%3D").replace("/", "%2F")
    url += '?' + "partner="+PARTNER_CODE+"&code="+qry.replace(" ","+") + "&format=json&filter=person&count=" + str(count) + '&sed=' + sed + '&sig=' + sig
    
    e = requests.get(url, headers=headers).text
    d = json.loads(e)["person"]["participation"]
    
    filmography = []
    for i in d:
      movie = {}
      if "movie" in i:
        
        movie["title"] = i["movie"]["title"]
        movie["productionYear"] = i["movie"]["productionYear"]
        movie["activity"] = i["activity"]["$"]
        
        if "role" in i:
          movie["role"] = i["role"]
        else:
          movie["role"] = ""
        
        filmography.append(movie)
    
    return filmography
    

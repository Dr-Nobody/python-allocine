
from datetime import date
import datetime
import Person
from settings import *
import requests, time, hashlib, sys, base64, json
from Review import Review

class Movie:


  def __init__(self, code):
    self.parameters = code
    
    self.code = code["code"]
    
    if "statistics" in code:
      if "userRating" in code["statistics"]:
        self.userRating = code["statistics"]["userRating"]
      else:
        self.userRating = "<unknown>"
        
      if "pressRating" in code["statistics"]:
        self.pressRating = code["statistics"]["pressRating"]
      else:
        self.pressRating = "<unknown>"
    else:
      self.userRating = "<unknown>"
      self.pressRating = "<unknown>"

    if "poster" in code:
      self.poster = code["poster"]["href"]
    else:
      self.poster = "<unknown>"
      
    if "productionYear" in code:
      self.productionYear = code["productionYear"]
    else:
      self.productionYear = "<unknown>"

    if "title" in code:
      self.title = code["title"]
    elif "originalTitle" in code:
      self.title = code["originalTitle"]
    else:
      self.title = "<unknown>"
      
    if "castingShort" in code:
      self.directors = code["castingShort"]["directors"]
      if "actors" in code["castingShort"]:
        self.actors = code["castingShort"]["actors"]
      else:
        self.actors = "<unknown>"
    else:
      self.directors = "<unknown>"
      self.actors = "<unknown>"
      
    if "release" in code:
      d = datetime.datetime.strptime(code["release"]["releaseDate"], '%Y-%m-%d')
      self.release = d.strftime('%d/%m/%Y')
    else:
      self.release = "<unknown>"

    if "link" in code:
      self.link = code["link"][0]["href"]
    else:
      self.link = "<unknown>"

    
    #if "synopsisShort" in code:
    #  self.synopsis = code["synopsisShort"]
    #else:
    #  self.synopsis = "<unknown>"
  
  
  def __unicode__(self):
    return self.title

  
  def __lt__(self, other):
    if self.userRating != "<unknown>" and other.userRating != "<unknown>":
      return float(self.userRating) < float(other.userRating)
    elif self.userRating == "<unknown>" and other.userRating != "<unknown>":
      return False
    elif self.userRating != "<unknown>" and other.userRating == "<unknown>":
      return True
    else:
      return False

  def get_reviewlist(self, count=10):
    headers = {"User-Agent":"Dalvik/1.6.0 (Linux; U; Android 4.2.2; Nexus 4 Build/JDQ39E)"}
    url = "http://api.allocine.fr/rest/v3/reviewlist"
        
    try:
        sed = str(date.today().strftime("%Y%m%d"))
        sig = hashlib.sha1(SECRET_KEY + "partner="+PARTNER_CODE+"&code=" + str(self.code) + "&type=movie&format=json&filter=public&count=" + str(count) + '&sed=' + sed).digest().encode("base64").replace("\n","").replace("+", "%2B").replace("=", "%3D").replace("/", "%2F")
        url += '?' + "partner="+PARTNER_CODE+"&code=" + str(self.code) + "&type=movie&format=json&filter=public&count=" + str(count) + '&sed=' + sed + '&sig=' + sig
        
    except UnicodeEncodeError:
        return []
    
    e = requests.get(url, headers=headers).text
    
    d = json.loads(e)
    feed = d["feed"]
    
    self.reviews = []
    
    if feed["totalResults"] > 0:
      
      if "review" in feed:
        for rev in feed["review"]:
          
          review2 = Review(rev)
          
          self.reviews.append(review2)
          
    else:
      self.reviews = []
    return self.reviews


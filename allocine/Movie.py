from AllocineObject import *
import Person

class Movie:

#  class Participation(object):
#    def __init__(self, activity, person):
#      self.activity = activity
#      self.person = person

  def __init__(self, code):
    self.code = code["code"]
    #print ">>>>", code
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
      d = datetime.strptime(code["release"]["releaseDate"], '%Y-%m-%d')
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
    
    try:
      return self.title
    except:
      try:
        return self.originalTitle
      except:
        return "untitled"

  def getInfo(self, profile = DEFAULT_PROFILE):
    super(Movie, self).getInfo(profile)
    if "castMember" in self.__dict__:
      castMember = []
      for i in self.castMember:
        if "person" in i:
          code = i["person"]["code"]
          i["person"].pop("code")
          p = Person.Person(code, **(i["person"]))
          castMember.append(self.Participation(i["activity"], p))
      self.castMember = castMember

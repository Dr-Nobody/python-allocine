

class Review:


  def __init__(self, code):
    self.parameters = code
    
    self.code = code["code"]
    self.body = code["body"]
    self.rating = code["rating"]
    self.reviewUrl = code["reviewUrl"]
    self.writer = code["writer"]["name"]
    self.creationDate = code["creationDate"]
  
  
  def __unicode__(self):
    return self.body
    



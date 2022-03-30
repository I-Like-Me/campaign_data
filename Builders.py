class NPC:
  def __init__(self, name, entry_ID, age="--unknown--", job="--unknown--", group="--unknown--", relationship=5, home_location="--unknown--", origin="--unknown--", congress_member=False):
    self.name = name
    self.entry_ID = entry_ID
    self.age = age
    self.job = job
    self.group = group
    self.relationship = relationship
    self.home_location = home_location
    self.origin = origin
    self.congress_member = congress_member
  
  def __repr__(self):
    return f"""{self.name} is a {self.job}
"""
    
  def set_age(self, new_age):
    self.age = new_age
    
  def set_job(self, new_job):
    self.job = new_job

  def set_group(self, new_group):
    self.group = new_group
    
  def set_relationship(self, new_relationship):
    self.relationship = new_relationship

  def set_home_location(self, new_home_location):
    self.home_location = new_home_location
    
  def set_origin(self, new_origin):
    self.origin = new_origin

  def set_congress_member(self, new_congress_member):
    self.congress_member = new_congress_member
    
#--------------------------------------------------    
    
class event:
  def __init__(self, label, date="--unknown--", involved="--unknown--", present=False):
    self.label = label
    self.date = date
    self.involved = involved
    self.present = present
  

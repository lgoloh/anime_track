'''
Created on Jan 20, 2018

@author: Leslie
'''

class AnimeData:
    def __init__(self, icon, date, episode):
        self.icon = icon
        self.date = date
        self.episode = episode
    
    def get_icon(self):
        return self.icon
    
    def get_date(self):
        return self.date
    
    def get_episode(self):
        return self.episode
        
    def __str__(self):
        return "<Poster: %s, Date: %s, Episode: %s>" % (self.icon, self.date, self.episode) 

        

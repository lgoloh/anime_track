'''
Created on Jan 20, 2018

@author: Leslie
'''

import sys
#mport urllib.request
from urllib.request import Request, urlopen, urlretrieve
from bs4 import BeautifulSoup 
import datetime
import calendar
from ani_Objects import AnimeData
import os




#Get current month and year
def current_date():
    now = datetime.datetime.now()
    return (now.strftime("%B"), now.strftime("%Y"))


#overwriting the print function because of encoding issues.
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

#dictionary of seasons
mon = calendar.month_name
seasons = {'Spring':(mon[3],mon[4],mon[5]), 'Summer':(mon[6],mon[7],mon[8]), 'Fall':(mon[9],mon[10],mon[11]), 'Winter':(mon[12],mon[1],mon[2])}

#gets the season of the current date
def get_Season(seasons, mon):
    curr_date = current_date()  #curr_date is a tuple of the month and year
    month = mon[curr_date[0]]
    for key in seasons:
        for value in seasons[key]:
            if value == month:
                return key

def get_Year():
    curr_date = current_date()
    return curr_date[1]
    


#overwrite the User-Agent header defined by urlopener
    
#Query the website and return html of the website and store it in the variable temp

def fetch_url(url):
    temp = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    anime = urlopen(temp).read()
    return anime
#Parse the html of the website and store in a Beautiful Soup format, lxml is an html parser

def parse_html(html):
    soup = BeautifulSoup(html, "lxml")
    return soup


def get_seasons(soup):    
    season = soup.find_all("article")
    return season
     

#get all the anime posters
def get_posters(soup):
    posters = soup.find_all("div", class_="poster-container")
    return posters


def store_icons(posters):
    b = "/"
    i = 0
    uprint (posters)
    for p in posters:
        icon = p.img["src"]
        name = p.img["alt"]
        if b in name:
            while i < len(name):
                uprint
                if name[i] == b:
                    uprint("True")
                    name[i] = " "  
        path = os.path.join("C:/Users\\Leslie\\Desktop\\AnimeTrac\\icon_resource", name) 
        urlretrieve(icon, path)

   
#get the dates
def get_dates(soup):
    dates = soup.find_all("div", class_="anime-date")
    return dates

#get the number of episodes
def get_episodes(soup):
    episodes = soup.find_all("div", class_="anime-episodes")
    return episodes

#get all winter chart links
def get_charts(soup):
    all_charts = soup.select("ul.dropdown-menu a")
    return all_charts

def get_prefix():
    return "https://www.livechart.me"

def all_links(all_charts, prefix):
    links = []
    for a in all_charts:
        if ("Winter" in a.get_text())|("Summer" in a.get_text()) | ("Spring" in a.get_text()) | ("Fall" in a.get_text()):
            links.append(prefix + a["href"])
    return links


def winter_links(all_charts, prefix):
    links = []
    for a in all_charts:
        if "Winter" in a.get_text():
            links.append(prefix + a["href"])
    return links




def summer_links(all_charts, prefix):
    links = []
    for a in all_charts:
        if "Summer" in a.get_text():
            links.append(prefix + a["href"])
    return links



def spring_links(all_charts, prefix):
    links = []
    for a in all_charts:
        if "Spring" in a.get_text():
            links.append(prefix + a["href"])
    return links



def fall_links(all_charts, prefix):
    links = []
    for a in all_charts:
        if "Fall" in a.get_text():
            links.append(prefix + a["href"])
    return links





def create_anime_object(posters, dates, episodes):
    anime_objects = []
    i=0
    while i < len(posters):
        anijet = AnimeData(posters[i].img["src"], dates[i].get_text(), episodes[i].get_text())
        anime_objects.append(anijet)
        i+=1
    return anime_objects 
  
  

def all_anime(posters, dates, episodes, season):
    all_winter_anime={}
    i = 0
    post = posters
    date = dates
    eps = episodes
    anime_objects = create_anime_object(post, date, eps)
    for an_article in season:
        all_winter_anime[an_article.h3.get_text()] = anime_objects[i]
        i+=1
    return all_winter_anime


def get_Anime(url):
    anime_html = fetch_url(url)
    anime_soup = parse_html(anime_html)
    posters = get_posters(anime_soup)
    store_icons(posters)
    uprint(posters)
    dates = get_dates(anime_soup)
    episodes = get_episodes(anime_soup)
    season = get_seasons(anime_soup)
    anime = all_anime(posters, dates, episodes, season)
    return anime
    

anime = get_Anime("https://www.livechart.me/winter-2018/tv")
uprint(anime)
for a in anime:
    uprint(anime[a])

    
'''    
    
Event Handlers 
These are the functions that will be called when the corresponding button is pressed.
They will return the anime for the current year 

'''


''' Handlers for year buttons '''
def get_Summer(charts, prefix):
    curr_yr = get_Year()
    summer = summer_links(charts, prefix)
    for link in summer:
        if curr_yr in link:
            return get_Anime(link)

def get_Winter(charts, prefix):
    curr_yr = get_Year()
    winter = winter_links(charts, prefix)
    for link in winter:
        if curr_yr in link:
            return get_Anime(link)
        
def get_Spring(charts, prefix):
    curr_yr = get_Year()
    spring = spring_links(charts, prefix)
    for link in spring:
        if curr_yr in link:
            return get_Anime(link)

def get_Fall(charts, prefix):
    curr_yr = get_Year()
    fall = fall_links(charts, prefix)
    for link in fall:
        if curr_yr in link:
            return get_Anime(link)

    

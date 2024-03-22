import requests
import json
from bs4 import BeautifulSoup
match_url = "https://www.fotmob.com/matches/atlas-vs-monterrey/1pykrs#4384470"
r = requests.get(match_url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
json_fotmob = json.loads(soup.find("script", attrs={"id":"__NEXT_DATA__"}).contents[0])
shotmap = json_fotmob["props"]["pageProps"]["content"]["shotmap"]
xG = [shot["expectedGoals"] for shot in shotmap["shots"]]
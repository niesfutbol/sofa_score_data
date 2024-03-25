import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
match_url = "https://www.fotmob.com/matches/puebla-vs-fc-juarez/2r8ak7wr#4384438"
r = requests.get(match_url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
json_fotmob = json.loads(soup.find("script", attrs={"id":"__NEXT_DATA__"}).contents[0])
shotmap = json_fotmob["props"]["pageProps"]["content"]["shotmap"]
xG = pd.DataFrame(shotmap["shots"])
xG.to_csv("xg_puebla_juarez.csv", index = False)

statistics = json_fotmob["props"]["pageProps"]["content"]["stats"]["Periods"]["All"]["stats"][0]["stats"]
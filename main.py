import json
import requests
from bs4 import BeautifulSoup as BS
from datetime import date
import pandas as pd


def infoGames(team, year):
    if 2013 < year <= date.today().year:
        urlBase = "https://understat.com/league/Serie_A/"
        URL = urlBase + str(year)
        r = requests.get(URL)
        soup = BS(r.content, 'lxml')
        scripts = soup.find_all('script')
        strings = scripts[1].string
        json_data = strings[strings.index("('") + 2: strings.index("')")]
        json_data = json_data.encode("utf-8").decode('unicode escape')
        data = json.loads(json_data)

        for each in data:
            if each['h']['title'] == team or each['a']['title'] == team:
                newEach = {}
                newEach['id'], newEach['isResult'], newEach['datetime'] = each['id'], each['isResult'], each['datetime']
                newEach['team1_id'], newEach['team1_title'], newEach['team1_short_title'] = each['h']['id'], each['h'][
                    'title'], each['h']['short_title']
                newEach['team2_id'], newEach['team2_title'], newEach['team2_short_title'] = each['a']['id'], each['a'][
                    'title'], each['a']['short_title']
                newEach['team1_goals'], newEach['team2_goals'] = each['goals']['h'], each['goals']['a']
                newEach['team1_xG'], newEach['team2_xG'] = each['xG']['h'], each['xG']['a']
                print(f"{pd.Series(newEach)}\n")




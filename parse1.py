import json
import requests
from bs4 import BeautifulSoup as BS
from datetime import date


def infoGames(team, year):
    if 2013 < year <= date.today().year:
        urlBase = "https://understat.com/league/Serie_A/"
        URL = urlBase + str(year)
        r = requests.get(URL)
        soup = BS(r.content, 'lxml')
        scripts = soup.find_all('script')
        strings = scripts[1].string
        indexStart = strings.index("('") + 2
        indexEnd = strings.index("')")
        json_data = strings[indexStart:indexEnd]
        json_data = json_data.encode("utf-8").decode('unicode escape')
        data = json.loads(json_data)
        print(data)
        for each in data:
            if each['h']['title'] == team:
                if each['isResult'] == True:
                    print(
                        f"Team: {each['h']['title']}\nShort title {each['h']['short_title']}Game ID: {each['h']['id']}\n"
                        f"Rival team: {each['a']['title']}\nShort name of rival team: {each['a']['short_title']}\n"
                        f"Goals: {each['goals']['h']}:{each['goals']['a']}\nDate of game: {each['datetime']}\n"
                        f"Forecast: {each['forecast']}\n")
                else:
                    print(
                        f"Team: {each['h']['title']}\nShort title {each['h']['short_title']}Game ID: {each['h']['id']}\n"
                        f"Rival team: {each['a']['title']}\nShort name of rival team: {each['a']['short_title']}\n"
                        f"Date of game: {each['datetime']}\n")
    else:
        print("We can't help You: Invalid year!")


infoGames("Inter", 2021)





import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from main import infoGames


def playerInfo(name):
    url = "https://understat.com/league/Serie_A"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="lxml")
    scripts = soup('script')
    scriptLst = []
    for each in scripts:
        scriptLst.append(each)
    strings = scriptLst[3].string
    json_data = strings[strings.index("('") + 2: strings.index("')")]
    json_data = json_data.encode("utf-8").decode('unicode escape')
    data = json.loads(json_data)
    flt = re.compile(name.lower())
    for playerData in data:
        if flt.match(playerData['player_name'].lower()):
            print(pd.Series(playerData))




def main():
    con = input("Hi. There you can find football info about italian Serie A: You want to continue?\n"
          "yes - y and another button, for exit!")
    if con == 'y':
       choice = input("Info about games - 1\nInfo about player - 2\n")
       if choice == '1':
           team = input("Team name: ")
           year = int(input("year from 2014 to this year: "))
           infoGames(team, year)
       elif choice == "2":
           name = input("Player name: ")
           playerInfo(name)
       else:
           print("Put 1 or 2!")
       main()

    else:
        print('Bye!')



if __name__ == '__main__':
    main()
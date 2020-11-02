import requests
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import comparison_practice as comp_graph
import pickle

head = {'Host': 'stats.nba.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
'Accept': 'application/json, text/plain, /',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'x-nba-stats-origin': 'stats',
'x-nba-stats-token': 'true',
'Connection': 'keep-alive',
'Referer': 'https://stats.nba.com/',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'}


link_advanced = 'https://stats.nba.com/stats/leaguedashlineups?Conference=&DateFrom=' \
       '&DateTo=&Division=&GameID=&GameSegment=&GroupQuantity=5&LastNGames=0' \
       '&LeagueID=00&Location=&MeasureType=Advanced&Month=0&OpponentTeamID=0' \
       '&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N' \
       '&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=' \
       '&TeamID=1610612760&VsConference=&VsDivision='

link_opponent = 'https://stats.nba.com/stats/leaguedashlineups?Conference=&DateFrom=' \
       '&DateTo=&Division=&GameID=&GameSegment=&GroupQuantity=5&LastNGames=0' \
       '&LeagueID=00&Location=&MeasureType=Opponent&Month=0&OpponentTeamID=0' \
       '&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlusMinus=N' \
       '&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=' \
       '&TeamID=1610612760&VsConference=&VsDivision='


thunder_id = '16106127'


response_advanced = requests.get(link_advanced, headers=head)
response_opponent = requests.get(link_opponent, headers=head)
headers_advanced = response_advanced.json()['resultSets'][0]['headers']
headers_opponent = response_opponent.json()['resultSets'][0]['headers']
stats_advanced = response_advanced.json()['resultSets'][0]['rowSet']
stats_opponent = response_opponent.json()['resultSets'][0]['rowSet']

df_advanced = pd.DataFrame(stats_advanced, columns=headers_advanced)
df_opponent = pd.DataFrame(stats_opponent, columns=headers_opponent)

df_final = df_advanced.merge(df_opponent, on='GROUP_NAME', how='left')

print(tabulate(df_final.head(), headers='keys', tablefmt = 'psql'))

big_four = ['Adams,Steven', 'Westbrook,Russell', 'George,Paul', 'Anthony,Carmelo']
big_five = ['Adams,Steven', 'Westbrook,Russell', 'George,Paul', 'Anthony,Carmelo', 'Roberson,Andre']
stats_for_collection = ['DEF_RATING',
                        'NET_RATING',
                        'OPP_FG3_PCT',
                        'OPP_FG_PCT']

def intersect(lis1, lis2):
    return list(set(lis1) & set(lis2))

master_dict = dict()
for stat in stats_for_collection:
    def_min_list = list()
    roberson = 0
    for index, row in df_final.iterrows():
        lineup = row['GROUP_NAME'].split(' - ')
        #lineup = [str(name, 'utf-8') for name in lineup]
        if(len(intersect(big_five, lineup)) == 5):
            roberson = row[stat]
        if(len(intersect(big_four, lineup)) == 4):
            if 'Roberson,Andre' not in lineup:
                print(row['MIN_x'])
                def_min = [row[stat], row['MIN_x']]
                def_min_list.append(def_min)
    total_minutes = 0
    minutes_def = 0
    for player in def_min_list:
        minutes_def += player[0] * player[1]
        total_minutes += float(player[1])
    avg_def = minutes_def / total_minutes
    master_dict[stat] = [roberson, avg_def]

print(stats_for_collection)

fig, ax = plt.subplots(nrows=2, ncols=len(master_dict))
col = 0
for stat in master_dict:
    print(stat)
    comp_graph.create_subplot(stat, col, master_dict[stat], "red", "blue")
    col = col + 1
plt.subplots_adjust(wspace = 0.2, hspace = 0.2)
plt.show()








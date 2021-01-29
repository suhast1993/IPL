import random
import pandas as pd
import numpy as np

'''
CSK = ['CSK',8,4,0.233,0]
DC = ['DC',8,4,-0.133,0]
MI = ['MI',7,4,0.537,0]
SRH = ['SRH',5,6,0.559,0]
KXIP = ['KXIP',5,6,-0.117,0]
RR = ['RR',5,7,-0.321,0]
KKR = ['KKR',4,7,-0.050,0]
RCB = ['RCB',4,8,-0.694,0]
'''
IPLteams1 = {'CSK': [5,8,-0.532,10], 'DC': [7,6,-0.159,14], 'MI': [9,4,1.296,18], 'SRH': [6,7,0.555,12],
'KXIP': [6,7,-0.133,12], 'RR': [6,7,-0.377,12], 'KKR': [6,7,-0.467,12], 'RCB': [7,6,-0.145,14]}

IPLteams = pd.DataFrame(IPLteams1,index = ['W','L','RR','Points'])

def play(team1,team2):
    if random.randint(1,100) > 50:
        IPLteams[team1][0] = IPLteams[team1][0] + 1
        IPLteams[team1][3] = IPLteams[team1][3] + 2
        IPLteams[team2][1] = IPLteams[team2][1] + 1
        x = np.random.normal(0.336,0.2445,1)
        IPLteams[team1][2] = IPLteams[team1][2] + x
        IPLteams[team2][2] = IPLteams[team2][2] - x
    else:
        IPLteams[team2][0] = IPLteams[team2][0] + 1
        IPLteams[team2][3] = IPLteams[team2][3] + 2
        IPLteams[team1][1] = IPLteams[team1][1] + 1
        x = np.random.normal(0.336,0.2445,1)
        IPLteams[team2][2] = IPLteams[team2][2] + x
        IPLteams[team1][2] = IPLteams[team1][2] - x

games = [['CSK','KXIP'], ['KKR','RR'], ['DC','RCB'], ['SRH','MI']]

Finaltally = pd.DataFrame({'CSK': [0], 'DC': [0], 'MI': [0], 'SRH': [0], 'KXIP': [0], 'RR': [0], 'KKR': [0], 'RCB': [0]})

def rungames():
    for game in games:
        play(game[0],game[1])

def qualified(teams):
    teams1 = teams.transpose()
    teams2 = teams1.nlargest(4,['Points', 'RR'])
    for team in teams2.index:
        if team == 'CSK':
            Finaltally['CSK'] = Finaltally['CSK'] + 1
        if team == 'DC':
            Finaltally['DC'] = Finaltally['DC'] + 1
        if team == 'MI':
            Finaltally['MI'] = Finaltally['MI'] + 1
        if team == 'SRH':
            Finaltally['SRH'] = Finaltally['SRH'] + 1
        if team == 'KXIP':
            Finaltally['KXIP'] = Finaltally['KXIP'] + 1
        if team == 'RR':
            Finaltally['RR'] = Finaltally['RR'] + 1
        if team == 'KKR':
            Finaltally['KKR'] = Finaltally['KKR'] + 1
        if team == 'RCB':
            Finaltally['RCB'] = Finaltally['RCB'] + 1

for i in range(10000):
    rungames()
    qualified(IPLteams)
    IPLteams = pd.DataFrame(IPLteams1,index = ['W','L','RR','Points'])

print(Finaltally/100)

'''
def qteams(teams):
    scores = IPLteams1

#for i in range(1000):
for game in games:
    playmatch(game[0],game[1])


def qteams(teams):
    scores
'''
import csv

class Player() :
    def __init__(self, name, age, team, ppg, rpg, apg):
        self.name = name
        self.age = age
        self.team = team
        self.ppg = ppg
        self.rpg = rpg
        self.apg = apg

    def listStats(self):
        print(self.name + " is " + self.age + " years old, and averaged " + self.ppg + " points per game, " + self.rpg + " rebounds per game and " + self.apg + " assists per game this season for the " + self.team + ".")

with open('Seasons_Stats.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    lineCount = 0
    for row in csvReader:
        print(f'\t{row[2]} played in {row[1]} for the {row[5]}')
        lineCount += 1

lebronJames = Player("Lebron James", "34", "LAL", "27.4", "8.5", "8.3")
lebronJames.listStats()

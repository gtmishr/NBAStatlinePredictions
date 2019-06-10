import csv

class Player() :
    def __init__(self, name, age, year, team, points, rebounds, assists):
        self.name = name
        self.age = age
        self.year = year
        self.team = team
        self.points = points
        self.rebonds = rebounds
        self.assists = assists

    def listStats(self):
        print(self.name + " is " + self.age + " years old, and averaged " + self.points + " points per game, " + self.rebounds + " rebounds per game and " + self.assists + " assists per game this season for the " + self.team + ".")

with open('Seasons_Stats.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    lineCount = 0
    playersArray = []
    parsedRebounds = 0

    for row in csvReader:
        print(f'\t{row[2]} played in {row[1]} for the {row[parsedRebounds]}')

        if {row[47]} != int:
            parsedRebounds = 0
        else:
            parsedRebounds = {row[47]}

        playersArray.append(Player(f'{row[2]}', f'{row[4]}', f'{row[1]}', f'{row[5]}', f'{row[52]}', f'{row[48]}', parsedRebounds))

        lineCount += 1

for i in len(playersArray):
    playersArray[i].listStats()

playersArray.append(Player("Lebron James", "34", "2019", "LAL", "27.4", "8.5", "8.3"))

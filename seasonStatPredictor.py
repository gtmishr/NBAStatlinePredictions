import csv
from sklearn import tree

class Player() :
    def __init__(self, name, age, year, team, gamesPlayed, points, assists):
        self.name = name
        self.age = age
        self.year = year
        self.team = team
        self.gamesPlayed = gamesPlayed
        self.points = points
        self.assists = assists

    def listStats(self):

        print(self.name + " is " + self.age + " years old, played " + self.gamesPlayed + " games, and scored " + self.points + " points, and " + self.assists + " assists this season for the " + self.team + ".")

def createPlayerObject(firstUserNameSearch, secondUserNameSearch):

    with open('Seasons_Stats.csv') as csvFile:

        csvReader = csv.reader(csvFile, delimiter = ',')
        lineCount = 0
        parsedRebounds = 0

        for row in csvReader:

            if (firstUserNameSearch.lower() == f'{row[2]}'.lower()) or (secondUserNameSearch.lower() == f'{row[2]}'.lower()):

                statsArray.append([(float(f'{row[52]}')/float(f'{row[6]}')), (float(f'{row[47]}')/float(f'{row[6]}')), (float(f'{row[46]}')/float(f'{row[6]}')), float(f'{row[36]}'), float(f'{row[39]}')])
                playersNamesArray.append(f'{row[2]}')

                lineCount += 1

statsArray = []
playersNamesArray = []

firstUserNameSearch = input("Enter a player's name: ")
secondUserNameSearch = input("Now enter another player's name: ")
createPlayerObject(firstUserNameSearch, secondUserNameSearch)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(statsArray, playersNamesArray)

print(clf.predict([[28, 10, 10, 0.4, 0.3]]))
print(clf.predict([[4, 0, 6, 0.2, 0.5]]))

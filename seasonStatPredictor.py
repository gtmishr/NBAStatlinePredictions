import csv
from sklearn import tree
from sklearn.tree.export import export_text

def opening():

    statsArray = []
    playersNamesArray = []

    initialInput = input("Welcome! What would you like to do? ")

    if (initialInput.lower() == "List Stats".lower()) or (initialInput.lower() == "L".lower()) or (initialInput.lower() == "list".lower()):
        listPlayerStats()
    elif (initialInput.lower() == "2 Player Analysis".lower()) or (initialInput.lower() == "2P".lower()):
        twoPlayerPrediction()
    elif (initialInput.lower() == "Exit".lower()) or (initialInput.lower() == "E".lower()):
        print("Thanks for checking me out!")
        quit()

# Points scored / games, assists / games, rebounds / games, three point percentage, two point percentage
def createPlayerObjects(row):
    statsArray.append([(float(f'{row[52]}')/float(f'{row[6]}')), (float(f'{row[47]}')/float(f'{row[6]}')), (float(f'{row[46]}')/float(f'{row[6]}')), float(f'{row[36]}'), float(f'{row[39]}')])
    playersNamesArray.append(f'{row[2]}')

def listPlayerStats():

    with open('Seasons_Stats.csv') as csvFile:

        csvReader = csv.reader(csvFile, delimiter = ',')
        listLineCount = 0

        for row in csvReader:

            if (row[0] != "") and (f'{row[46]}' != ""):

                createPlayerObjects(row)

    print(statsArray)
    print(playersNamesArray)

    opening()

def twoPlayerPrediction():

    firstUserNameSearch = input("Enter a player's full name: ")
    secondUserNameSearch = input("Now enter another player's full name: ")

    with open('Seasons_Stats.csv') as csvFile:

        csvReader = csv.reader(csvFile, delimiter = ',')
        aLineCount = 0

        for row in csvReader:

            if (firstUserNameSearch.lower() == f'{row[2]}'.lower()) or (secondUserNameSearch.lower() == f'{row[2]}'.lower()):

                createPlayerObjects(row)
                aLineCount += 1

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(statsArray, playersNamesArray)

    r = export_text(clf, ["ppg", "apg", "rpg", "3p%", "2p%"])
    print(r)

    print(clf.predict([[30, 6, 9, 0.4, 0.3]]))
    print(clf.predict([[4, 0, 6, 0.2, 0.2]]))

    opening()

# Upon opening the program...

statsArray = []
playersNamesArray = []

opening()

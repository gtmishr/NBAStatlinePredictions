import csv
from sklearn import tree
from sklearn.tree.export import export_text

def opening():
# Function ran upon initial running of the program, and after each program is fully executed.

# "List Stats", "List", or "L" to access the listPlayerStats function, "2 Player Analysis", or "2P" to access the twoPlayerPrediction function, "Position Analysis" or "PA" to access the positionAnalysis function, and "Exit", or "E" to exit the program.

    statsArray.clear()
    playersNamesArray.clear()
    positionArray.clear()

    initialInput = input("Welcome! What would you like to do? ")

    if (initialInput.lower() == "List Stats".lower()) or (initialInput.lower() == "L".lower()) or (initialInput.lower() == "List".lower()):
        listPlayerStats()
    elif (initialInput.lower() == "2 Player Analysis".lower()) or (initialInput.lower() == "2P".lower()):
        twoPlayerPrediction()
    elif (initialInput.lower() == "Position Analysis".lower()) or (initialInput.lower() == "PA".lower()):
        positionAnalysis()
    elif (initialInput.lower() == "Exit".lower()) or (initialInput.lower() == "E".lower()):
        print("Thanks for checking me out!")
        quit()

def createPlayerObjectsFiveStat(row):
# Uses just points scored / games, assists / games, rebounds / games, three point percentage, two point percentage and is linked to an according array containing the name of the player(s).

    statsArray.append([(float(f'{row[52]}')/float(f'{row[6]}')), (float(f'{row[47]}')/float(f'{row[6]}')), (float(f'{row[46]}')/float(f'{row[6]}')), float(f'{row[36]}'), float(f'{row[39]}')])
    playersNamesArray.append(f'{row[2]}')

def createPlayerObjectsAllStats(row):
# CURRENTLY DOESN'T WORK
# Uses every statistic that doesn't contain a letter / twoPlayerPrediction, and is linked to an according array containing the position of a certain player.

    tempArray = []
    x = 0

    while x < 43:
        if f'{row[0]}' != '' and f'{row[x]}' != '' and (x != 0) and (x != 2) and (x != 3) and (x != 5) and (x != 7) and (x != 21) and (x != 26) and  (int(f'{row[x]}') >= 1980):
            tempArray.append(f'{row[x]}')
        playersNamesArray.append(f'{row[3]}')
        statsArray.append(tempArray)
        x += 1

def listPlayerStats():
# CURRENTLY DOESN'T WORK
# Goes through each player and lists their stats in a somewhat easy to read format.

    with open('Seasons_Stats.csv') as csvFile:

        csvReader = csv.reader(csvFile, delimiter = ',')
        listLineCount = 0

        for row in csvReader:

            if (row[0] != "") and (f'{row[46]}' != ""):

                createPlayerObjectsFiveStat(row)

    opening()

def twoPlayerPrediction():
# User inputs two names, and their statlines are collected from the createPlayerObjectsFiveStat function. Then, a decision tree is created between the names of the players and a statline is given for which it is predicted which of the two players would perform that statline.

    firstUserNameSearch = input("Enter a player's full name: ")
    secondUserNameSearch = input("Now enter another player's full name: ")

    with open('Seasons_Stats.csv') as csvFile:

        csvReader = csv.reader(csvFile, delimiter = ',')
        aLineCount = 0

        for row in csvReader:

            if (firstUserNameSearch.lower() == f'{row[2]}'.lower()) or (secondUserNameSearch.lower() == f'{row[2]}'.lower()):

                createPlayerObjectsFiveStat(row)
                aLineCount += 1

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(statsArray, playersNamesArray)

    r = export_text(clf, ["ppg", "apg", "rpg", "3p%", "2p%"])
    print(r)

    print(clf.predict([[30, 6, 9, 0.4, 0.3]]))
    print(clf.predict([[0, 0, 0, 0, 0]]))

    opening()

def positionAnalysis():
# CURRENTLY DOESN'T WORK
# Gets the statistics from createPlayerObjectsAllStats function and uses it's correlation with their positions to find the barriers to each position.

    with open('Seasons_Stats.csv') as csvFile:

        csvReader = csv.reader(csvFile, delimiter = ',')
        pLineCount = 0

        for row in csvReader:
            createPlayerObjectsAllStats(row)
            pLineCount += 1

        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(statsArray, positionArray)

        r = export_text(clf, ["year", "position", "age", "games played", "minutes played", "per", "ts%", "3par", "ftr", "orb%", "drb%", "trb%", "ast%", "stl%", "blk%", "tov%", "usg%", "ows", "dws", "ws", "ws/48", "obpm", "dbpm", "bpm", "vorp", "fg", "fga", "fg%", "3p", "3pa", "3p%", "2p", "2pa", "2p%", "efg%", "ft", "fta", "ft%"])
        print(r)



        opening()

# Upon opening the program...

statsArray = []
playersNamesArray = []
positionArray = []

opening()

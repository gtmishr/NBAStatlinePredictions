import csv
from sklearn import tree

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

def createPlayerObjects(row):
    statsArray.append([(float(f'{row[52]}')/float(f'{row[6]}')), (float(f'{row[47]}')/float(f'{row[6]}')), (float(f'{row[46]}')/float(f'{row[6]}')), float(f'{row[36]}'), float(f'{row[39]}')])
    playersNamesArray.append(f'{row[2]}')

def listPlayerStats(): # This currently doesn't work, but we'll get to it. I have to do actual homework now anyways.

        with open('Seasons_Stats.csv') as csvFile:

            csvReader = csv.reader(csvFile, delimiter = ',')
            lineCount = 0
            parsedRebounds = 0

            for row in csvReader:

                createPlayerObjects(lineCount)
                lineCount += 1

                print(statsArray[row])
                print(playersNamesArray[row])

            opening()

def twoPlayerPrediction():

    firstUserNameSearch = input("Enter a player's full name: ")
    secondUserNameSearch = input("Now enter another player's full name: ")

    with open('Seasons_Stats.csv') as csvFile:

        csvReader = csv.reader(csvFile, delimiter = ',')
        lineCount = 0
        parsedRebounds = 0

        for row in csvReader:

            if (firstUserNameSearch.lower() == f'{row[2]}'.lower()) or (secondUserNameSearch.lower() == f'{row[2]}'.lower()):

                createPlayerObjects(row)
                lineCount += 1

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(statsArray, playersNamesArray)

    print(clf.predict([[28, 10, 10, 0.4, 0.3]]))
    print(clf.predict([[4, 0, 6, 0.2, 0.5]]))

    opening()

# Upon opening the program...

statsArray = []
playersNamesArray = []

opening()

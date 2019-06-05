import csv

with open('Seasons_Stats.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ',')
    lineCount = 0
    for row in csvReader:
        print(f'\t{row[2]} played in {row[1]} for the {row[5]}')
        lineCount += 1

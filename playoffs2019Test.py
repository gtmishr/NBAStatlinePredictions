from sklearn import tree

# [Points, rebounds, assists, steals, blocks]
# First 6 are Kawhi Leonard's games in the 2019 NBA Eastern Conference Finals against the Milwakee Bucks. Second 6 are Shai Gilgeous-Alexander in the 2019 Playoffs Round 1. I chose these two because they have a stark comparison in statistics (and I'm a Clippers fan).

features = [[31, 9, 2, 3, 0], [31, 8, 2, 0, 1], [36, 9, 5, 2, 1], [19, 7, 1, 4, 2], [35, 7, 9, 2, 0], [27, 17, 7, 2, 2], [18, 5, 1, 0, 3], [4, 0, 5, 4, 0], [7, 1, 2, 1, 1], [25, 2, 2, 1, 0], [6, 3, 3, 0, 0], [22, 5, 6, 0, 1]]
labels = ["Kawhi", "Kawhi", "Kawhi", "Kawhi", "Kawhi", "Kawhi", "Shai", "Shai", "Shai", "Shai", "Shai", "Shai"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[14, 0, 8, 2, 2]]))
print(clf.predict([[37, 17, 9, 4, 2]]))

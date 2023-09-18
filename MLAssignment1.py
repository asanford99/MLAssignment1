#-------------------------------------------------------------------------
# AUTHOR: Andrew Sanford
# FILENAME: MLAssignment1.py
# SPECIFICATION: Inputs a CSV file and outputs a Tree Diagram
# FOR: CS 4210- Assignment #1
# TIME SPENT: 2 Hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from itertools import count
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here

features = {
        "Young": 1,
        "Prepresbyopic": 2,
        "Presbyopic": 3,
        "Myope": 1,
        "Hypermetrope": 2,
        "Yes": 1,
        "No": 2,
        "Reduced": 1,
        "Normal": 2,
    }

X = []

for i in range(len(db)):
    X.append([])
    X[i].append(features[db[i][0]])
    X[i].append(features[db[i][1]])
    X[i].append(features[db[i][2]])
    X[i].append(features[db[i][3]])



#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here

Y = []

for i in range(len(db)):
    if db[i][4] == "Yes":
        Y.append(1)
    else:
        Y.append(2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()

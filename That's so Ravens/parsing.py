import csv

with open('assets\quizz.csv') as csvfile:
    reader = csv.readereader(csvfile,delimiter=' ', quotechar='|')
    for row in reader:
        print ', '.join(row)


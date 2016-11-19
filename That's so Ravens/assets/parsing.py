import csv
def parsing(question):
    f = open('quizz.csv')
    quiz = csv.reader(f)
    Questions = []
    Answers_c = []
    Answers_w = []
    for row in quiz:
        Questions.append(row[0])
        Answers_w.append(row[2:5])
    f.close()
        
    




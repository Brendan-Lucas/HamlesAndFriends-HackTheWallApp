import csv
def parsing():
    f = open('QuizApp/quizAssets/quizz.csv')
    quiz = csv.reader(f)
    Questions = []
    Answers = []
    for row in quiz:
        Questions.append(row[0])
        Answers.append(row[1:5])
    f.close()
    return Questions, Answers


def blurb(questionNum):
    reader = csv.reader('QuizApp/quizAssets/Answers.scv')
    blurbs = []
    for rows in reader:
        blurbs.append(row)
    reader.close()
    return blurbs[questionNum]
    
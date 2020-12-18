import csv
import random


def questions(lst,totalLines):
    r = random.randint(0,int(totalLines)-1)
    if r == 0:
        questions(lst,totalLines)
    else:
        print(lst[r])


with open('C:/Users/Lenovo/Desktop/audio/q.csv',mode='r') as f:
    csvReader = csv.reader(f,delimiter="\n")
    lineCount = 0
    totalLines = 0
    lst = []
    for row in csvReader:
        lst.append(row)
        totalLines += 1
    questions(lst,totalLines)

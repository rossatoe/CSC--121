# -*- coding: utf-8 -*-
"""

"""

import csv
from dictQuestion import *
from M4HW_Dictionaries_rossatoe import *

def csvWriter(qNum):
    header = ["Question #", "Question", "Choice 1", "Choice 2", "Choice 3", "Answer"]
    try:
        
        with open("DinoTrivia.csv", "w", newline="") as csvFile:
            pen = csv.writer(csvFile, delimiter=",")
            pen.writerow(header)
            for question in questions.values():   
              print(qNum, "-", question["question"], "\n")
              row = [qNum, question["question"]]
              i = 1
              for choice in question["choices"]:
                print (i,")", choice)
                row.append(choice)
                i+=1
              #opt = int(input("\nEnter your choice number: "))
              row.append(question["answer"])
              #choices = question["choices"]
              #user_choice = choices[opt-1]
              #row.append(user_choice)
              pen.writerow(row)
              qNum += 1
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("Permission Denied (file open elsewhere)")

def txtWriter(qNum):
    i = 1
    #header = ["Question #", "Question", "Answer"]
    try:
        
        with open("DinoTrivia.txt", "w", newline="") as txtFile:
            txtFile.write(f'{"Question #":<15}{"Question":<100}{"Answer":<7}\n')
            for question in questions.values():
                txtFile.write(f'{i:<15}{question["question"]:<100}{question["answer"]}\n')
                i += 1
    except FileNotFoundError:
        print("File not found")
        


def main():
    print("")
    qNum = 1
    csvWriter(qNum)
    txtWriter(qNum)
    
    
    
    
if __name__ == "__main__":
    main()
    
    

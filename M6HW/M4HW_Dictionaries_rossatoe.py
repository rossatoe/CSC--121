# -*- coding: utf-8 -*-
"""
M4HW_Dictionaries
10/17/23
rossatoe
This program display a list of questions
"""
"""
ask user questions in loop
input answer
if it's correct display correct!
else display wrong!
     run + 1
if run < 3 break
display correct answers
display user answers
"""
from dictQuestion import *

def main():
    
    print("\tWelcome to the DinoTrivia!\n")
    answers = []
    run = 0
    qNum = 1
    for question in questions.values():
      print(qNum, "-", question["question"], "\n")
      i = 1
      for choice in question["choices"]:
        print (i,")", choice)
        i+=1
      opt = int(input("\nEnter your choice number: "))
      optText = question["choices"][opt-1]
      answers.append(optText)
      if optText == question["answer"]:
        print("\nCorrect!\n")
      else:
        print("\nWrong!\n")
        run +=1
      if run >= 3:
        print("You lost!")
        break
      qNum +=1
    if run < 3:
      print("You Won!")
    print("\nCorrect Answers: ", (len(answers)-run), "of 20.")
    print("\nYour Answers:")
    for answer in answers:
      print("\n", answer)
      
if __name__ == "__main__":
    main()
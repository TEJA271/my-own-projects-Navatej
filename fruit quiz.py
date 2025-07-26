import random

class fruitQuiz:
    def __init__ (self):
            self.fruit = {'apple':'red' ,
                                 "orange":"orange",
                                 "watermelon":"green",
                                 "bannana " : "yellow"}   
    def quiz(self):
      while (True):
            fruit , color = random.choice(list(self.fruits.items()))
            print("what is the coluor of {}".format(fruit))
            user_answer =input()
            if user_answer.lower() == color:
                  print("correct answer")
            else:
                  print("wrong answer")

            option = int(input("enter 0 , if you want to play again ,othervise enter 1"))
            if (option):
                  break
            
print("welcome to fruit quiz")
fq = fruitQuiz()
fq.quiz()
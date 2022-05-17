from turtle import *
import random
global score

print("Welcome to the game of champions or Jeopardy. You click on the number you want to play and the question will be asked to you. Remember that you start with what or who is and then say your answer and end your answer with a question mark. Once you finish a question and answer it, just click on another number and the question will be asked. DO NOT CLICK ON THE SAME NUMBER! You will penalized for your actions. Are your ready? Click a number, and if you click 'MYSTERY',you will be awarded or penalized with a random number of points.")
score=0
speed(0)
category_names=["Teachers","Suprise","Sports","Discipline","History"]

# Question/Answer Content
categories = [
  # Teachers
  [
    ["This person teaches history and football'", "Kieth Hellstern"],
    ["This person started a multi billion dollar company before Prep'", "Tom Shea"],
    ["This person stands in senior lot suring lunch'","Mr. Jones"],
    ["This person is the oldest teacher at Prep'", "Dr. Miller"]
  ],
  # Suprise
  [
    ["What time dose school end on halfdays","12:30"],
    ["who was the old owner of the levee'","claudio"],
    ["what time is B lunch over?","11:50"],
    ["When is \"Presedents holliday\"?", "superbowl monday"]
  ],
  
  # Sports
  [
    ["In what most recent year did Prep win hockey?", "2019"],
    ["This is the coach of Lacrosse?", "Grahm Neimi"],
    ["Who's Preps biggest rival", "Ludlowe"],
    ["What team at Prep holds the most titles", "Hockey"],
  ],
    # Discipline 
  [
    ["How many Jugs for a skip?", "3"],
    ["What does jug stand for?", "Justice Under God"],
    ["How many periods can you skip a day before a note goes home", "1"],
    ["How many infracions = jug", "3"],
  ],
    # History 
  [
    ["When was prep founded?", "1942"],
    ["What came first Fairfield U or Fairfield Prep", "Prep"],
    ["What rapper graduated from Prep?", "Felly"],
    ["Who founded Prep?", "Society of Jesuits"],
  ]
]



def insight():
  fd(200)
  lt(90)
  fd(200)
  lt(90)
  fd(80)
  lt(90)
  fd(400)
  lt(90)
  fd(80)
  lt(90)
  fd(100)
  lt(90)
  fd(400)
  bk(400)
  rt(90)
  fd(100)
  lt(90)
  fd(400)
  bk(400)
  rt(90)
  fd(100)
  lt(90)
  fd(400)
  bk(400)
  rt(90)
  fd(100)
  lt(90)
  fd(400)
  bk(240)
  lt(90)
  fd(400)
  lt(90)
  fd(80)
  bk(320)
  fd(160)
  lt(90)
  fd(400)
  lt(90)
  fd(80)
  lt(90)
  fd(400)
  rt(90)
  fd(80)
  rt(90)
  fd(400)
  bk(20)
  rt(90)
  fd(400)
def gameboard():
  insight()
gameboard()
def naming():
  penup()
# this writes the markings of points
  goto(-170,140)
  for b in range(4):
    for i in range(5):
      if i==1:
        penup()
        bk(15)
        write("MYSTERY")
        fd(15)
        pendown()
      else:  
        write((b+1)*100)
      penup()
      fd(80)
    penup()
    bk(400)
    rt(90)
    fd(95)
    lt(90)
    pendown()
  penup()
  goto(-175,185)
# this is the naming of the category names
  for category in category_names:
    write(category)
    fd(80)
naming()
def getgridposition(x,y):
  row = (200-y)//100
  col = (x+200)//80
  return [int(row),int(col)]
  
def whiteout(x,y):
  goto(x,y)
  color("white")
  pendown()
  backward(20)
  pensize (20)
  forward(40)
  pensize(5)
  penup()
def screenclicked(x, y):
  global score
  whiteout(x,y)
  # This function runs when the screen is clicked
  pos=getgridposition(x, y)
  
  row = pos[0]
  col = pos[1]
  
  a=input(categories[col][row][0])
  s=(categories[col][row][1])
  #if a.lower() == (categories[col][row][1])):
  if a.lower()== s.lower():
    if col==1:
      points=random.randrange(-1500,10000,50)
    else:  
      points= (row+1)*100
    print("Yes that's it you are rewarded " + str(points )+ " points")
    score=score+points
    print("This is your total score: " + str(score)+ " click on another box.")  
  else:
    if col==1:
      points=random.randrange(200,1050,50)
    else:  
      points= (row+1)*100
    print("Oh, that's not it, your score decreased by " + str(points))
    score=score-points
    print("This is your total score: " + str(score)+ " click on another box.")  
  
# Screen listens for click events

screen = getscreen()
screen.onclick(screenclicked)

screen.mainloop()

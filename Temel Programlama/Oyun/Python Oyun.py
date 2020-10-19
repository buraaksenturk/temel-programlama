import turtle
import math
import random

wn=turtle.Screen()
wn.bgcolor("lightblue")
wn.tracer(3)

cerceve=turtle.Turtle()
cerceve.penup()
cerceve.setposition(-300,-300)
cerceve.pendown()
cerceve.pensize(3)
for side in range(4):
    cerceve.fd(600)
    cerceve.left(90)
cerceve.hideturtle()

score=0
score_pen=turtle.Turtle()
score_pen.speed()
score_pen.color("black")
score_pen.penup()
score_pen.setposition(300,300)
scorestring="Score: %s" %score
score_pen.hideturtle()



oyuncu=turtle.Turtle()
oyuncu.color("white")
oyuncu.shape("triangle")
oyuncu.penup()
oyuncu.speed(0)




maxYem=15
yem=[]


for count in range(maxYem):
    yem.append(turtle.Turtle())
    yem[count].color("blue")
    yem[count].shape("circle")
    yem[count].pu()
    yem[count].speed(0)
    yem[count].setposition(random.randint(-300,300),random.randint(-300,300))
                   
maxYem2=8
yem2=[]


for count in range(maxYem2):
    yem2.append(turtle.Turtle())
    yem2[count].color("darkgreen")
    yem2[count].shape("circle")
    yem2[count].pu()
    yem2[count].speed(0)
    yem2[count].setposition(random.randint(-300,300),random.randint(-300,300))
    
speed=(1)

def turnleft():
    oyuncu.left(30)

def turnright():
    oyuncu.right(30)

def increasespeed():
    global speed
    speed +=1

def isCollision(t1,t2):
     d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor()-t2.ycor(),2))
     if d<20:
         return True
     else:
         return False
     
turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")


while True:
    oyuncu.forward(speed)
    if oyuncu.xcor()>300 or oyuncu.xcor()<-300:
        oyuncu.right(100)
    if oyuncu.ycor()>300 or oyuncu.ycor()<-300:    
        oyuncu.right(100)
        
    for count in range(maxYem):
        yem[count].fd(3)

        if yem[count].xcor()>300 or yem[count].xcor()<-300:
            yem[count].right(100)

        if yem[count].ycor()>300 or yem[count].ycor()<-300:
            yem[count].right(100)

        if isCollision(oyuncu,yem[count]):
            yem[count].setposition(random.randint(-300,300),random.randint(-300,300))
            yem[count].right(random.randint(0,360))
            score+=10
            score_pen.undo()
            scorestring="Score: %s" %score
            score_pen.write(scorestring ,False, align= "right",font=("Franklin Gothic Medium",30)) 

    for count in range(maxYem2):
        yem2[count].fd(3)

        if yem2[count].xcor()>300 or yem2[count].xcor()<-300:
            yem2[count].right(100)



        if yem2[count].ycor()>300 or yem2[count].ycor()<-300:
            yem2[count].right(100)


        if isCollision(oyuncu,yem2[count]):
            yem2[count].setposition(random.randint(-300,300),random.randint(-300,300))
            yem2[count].right(random.randint(0,360))
            score-=20
            score_pen.undo()
            scorestring="Score: %s" %score
            score_pen.color('white')
            style = ('Franklin Gothic Medium', 30, 'italic')
            score_pen.write(str(scorestring), font=style, align='center')



          
                
                



            

         


            
            

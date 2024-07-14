import turtle
import random
import pygame
import time


s = turtle.Turtle(shape = "circle")
s.hideturtle()
pygame.mixer.init()
WIDTH , HEIGHT = 500, 500

def turtles():
    colors = ["yellow", 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray', 'white']
    x = -215
    listn = []
    y = -190
    for i in range(4):
        for i in range(7):
            t = turtle.Turtle()
            t.color(random.choice(colors))
            t.shape("turtle")
            t.speed(1)
            t.penup()
            t.goto(x, y)
            listn.append(t)
            x += 70
        x = -215
        y += 30
    return listn

pen = turtle.Turtle()
pen.hideturtle()


def start_dance(x,y):
    s.hideturtle()
    s.clear()
    pen.clear()
    screen.bgpic("dance-floor.png")
    screen.update()
    pygame.mixer.music.load("dancin.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play()
    listn = turtles()
    time.sleep(12.5)
    while pygame.mixer.music.get_busy():
        for i in listn:
            y = i.ycor()
            x = i.xcor()
            i.penup()
            i.speed(0)
            if y % 2 ==0 and x % 2 !=0 or y % 2 !=0 and x % 2 ==0:
                i.right(random.randrange(20,60))
            else:
                i.left(random.randrange(20,60))
            if x <= -235 or x >= 235 or y >= -60 or y >= -240:
                if x <= -235: 
                    i.goto(x+10,y)
                if x >= 235:
                    i.goto(x-10,y)
                if y >= -60:
                    i.goto(x,y-10)
                if y <= -240:
                    i.goto(x,y+10)
            i.forward(random.randrange(1,10))
    turtle.bye()


def start():
    s.color('yellow')
    s.width(20)
    s.penup()
    s.goto(-100,0)
    s.pendown()
    s.forward(200)
    s.right(90)
    s.forward(20)
    s.right(90)
    s.forward(200)
    s.right(90)
    s.forward(18)
    s.right(90)
    s.forward(195)
    s.right(90)
    s.forward(8)
    s.showturtle()
    
    pen.color("black")
    pen.penup()
    pen.goto(-90, -25)
    pen.write("Click here - >", font=("Super Creamy", 20, "bold"))
    s.onclick(start_dance)









screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("white")
screen.title("Dance Floor")



start()







screen.mainloop()

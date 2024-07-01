import turtle
import random
import time
import pygame

screen = turtle.Screen()
screen.bgpic("background.png")
screen.title("Fireworks")
screen.setup(736,912)
pygame.mixer.init()
click = 0


firework_turtle = turtle.Turtle()
firework_turtle.hideturtle()
firework_turtle.speed(0)
firework_turtle.penup()
def firework_traces():
    listn = []
    x = 145
    for i in range(5):
        t = turtle.Turtle(shape="circle")
        t.hideturtle()
        t.color("black")
        t.penup()
        t.speed(0)
        t.goto(x,-262)
        listn.append(t)
        t.pendown()
        t.speed(1)
        x -= 75
    return listn
listn = firework_traces()

def draw_firework(x, y, color):
    firework_turtle.goto(x, y)
    firework_turtle.color(color)
    firework_turtle.begin_fill()
    for i in range(36):
        firework_turtle.color(color)
        firework_turtle.forward(130)
        firework_turtle.left(170)
    firework_turtle.end_fill()
    time.sleep(3)
    firework_turtle.clear()


def create_firework0(x,y):
    global click
    click += 1
    if click == 1:
        pygame.mixer.music.load("firework.mp3")
        pygame.mixer.music.play()
        trace = listn[0]
        x = random.randint(100, 200)
        y = random.randint(100, 300)
        colors = ["red", "yellow", "blue", "green", "purple", "orange"]
        color = random.choice(colors)
        trace.color(color)
        time.sleep(1)
        trace.showturtle()
        trace.goto(x+65,y)
        trace.hideturtle()
        draw_firework(x, y, color)
        trace.clear()
        trace.penup()
        trace.speed(0)
        trace.goto(145,-262)
        trace.pendown()
        trace.speed(1)
        click = 0
def create_firework1(x,y):
    global click
    click += 1
    if click == 1:
        pygame.mixer.music.load("firework.mp3")
        pygame.mixer.music.play()
        trace = listn[1]
        x = random.randint(0, 100)
        y = random.randint(100, 300)
        colors = ["red", "yellow", "blue", "green", "purple", "orange"]
        color = random.choice(colors)
        trace.color(color)
        time.sleep(1)
        trace.showturtle()
        trace.goto(x+65,y)
        trace.hideturtle()
        draw_firework(x, y, color)
        trace.clear()
        trace.penup()
        trace.speed(0)
        trace.goto(70,-262)
        trace.pendown()
        trace.speed(1)
        click = 0
def create_firework2(x,y):
    global click
    click += 1
    if click == 1:
        
        trace = listn[2]
        x = random.randint(-100, 0)
        y = random.randint(100, 300)
        colors = ["red", "yellow", "blue", "green", "purple", "orange"]
        color = random.choice(colors)
        trace.color(color)
        pygame.mixer.music.load("firework.mp3")
        pygame.mixer.music.play()
        time.sleep(1)
        trace.showturtle()
        trace.goto(x+65,y)
        trace.hideturtle()
        draw_firework(x, y, color)
        trace.clear()
        trace.penup()
        trace.speed(0)
        trace.goto(-5,-262)
        trace.pendown()
        trace.speed(1)
        click = 0
def create_firework3(x,y):
    global click
    click += 1
    if click == 1:
        pygame.mixer.music.load("firework.mp3")
        pygame.mixer.music.play()
        trace = listn[3]
        x = random.randint(-200, -100)
        y = random.randint(-100, 50)
        colors = ["red", "yellow", "blue", "green", "purple", "orange"]
        color = random.choice(colors)
        trace.color(color)
        time.sleep(1)
        trace.showturtle()
        trace.goto(x+65,y)
        trace.hideturtle()
        draw_firework(x, y, color)
        trace.clear()
        trace.penup()
        trace.speed(0)
        trace.goto(-80,-262)
        trace.pendown()
        trace.speed(1)
        click = 0
def create_firework4(x,y):
    global click
    click += 1
    if click == 1:
        pygame.mixer.music.load("firework.mp3")
        pygame.mixer.music.play()
        trace = listn[4]
        x = random.randint(-280, -200)
        y = random.randint(100, 300)
        colors = ["red", "yellow", "blue", "green", "purple", "orange"]
        color = random.choice(colors)
        trace.color(color)
        time.sleep(1)
        trace.showturtle()
        trace.goto(x+65,y)
        trace.hideturtle()
        draw_firework(x, y, color)
        trace.clear()
        trace.penup()
        trace.speed(0)
        trace.goto(-155,-262)
        trace.pendown()
        trace.speed(1)
        click = 0


def clickers():
    x = 170
    listn = []
    for i in range(5):
        t = turtle.Turtle(shape="circle")
        t.color("yellow")
        t.penup()
        t.speed(0)
        t.goto(x,-442)
        listn.append(t)
        x -= 75
    return listn

def launch_firework():
    listn = clickers()
    listn[0].onclick(create_firework0)
    listn[1].onclick(create_firework1)
    listn[2].onclick(create_firework2)
    listn[3].onclick(create_firework3)
    listn[4].onclick(create_firework4)



launch_firework()



screen.mainloop()

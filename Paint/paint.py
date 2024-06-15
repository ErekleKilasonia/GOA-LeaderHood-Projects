import turtle
import time
z = 'black'


def clickers(x,y):
    if x <= -880:
        pass
    elif x >= 540 and y >= 490:
        pass
    elif x <= -780 and y >= 250:
        pass
    elif x <= -330 and y >= 460:
        pass
    elif x >= 200 and y >= 480:
        pass
    elif x <= -450 and y >= 270:
        pass
    else:
        painter.goto(x,y)
def line_onclick(x,y):
    if x <= -528:
        painter.width(1)
        choser.goto(-551,502)
    elif x <= -481:
        painter.width(2)
        choser.goto(-501,502)
    elif x <= -428:
        painter.width(3)
        choser.goto(-451,502)
    elif x <= -381:
        painter.width(4)
        choser.goto(-401,502)
    else:
        painter.width(5)
        choser.goto(-351,502)



#screen

screen = turtle.Screen()
screen.setup(1920,1080)
screen.title('Paint')
screen.bgcolor('white')

def crcs(x,y):
    painter.circle(50)
def sqrs(x,y):
    painter.forward(50)
    painter.left(90)
    painter.forward(50)
    painter.left(90)
    painter.forward(50)
    painter.left(90)
    painter.forward(50)
    painter.left(90)


pes = turtle.Turtle()
pes.hideturtle()
pes._tracer(1,0)
pes.penup()
pes.goto(-700, 400)
pes.write("Draw Shapes", font=("Super Creamy", 30, "bold"))

pess = turtle.Turtle()
pess.hideturtle()
pess._tracer(1,0)
pess.penup()
pess.goto(-700, 340)
pess.write("Circle: ", font=("Super Creamy", 30, "bold"))


pess.goto(-530, 365)
pess.shape('circle')
pess.turtlesize(2)
pess.showturtle()
pess.onclick(crcs)

sqrt = turtle.Turtle()
sqrt.hideturtle()
sqrt._tracer(1,0)
sqrt.penup()
sqrt.goto(-700, 280)
sqrt.write("Square: ", font=("Super Creamy", 30, "bold"))

sqrt.goto(-500, 305)
sqrt.shape('square')
sqrt.turtlesize(2)
sqrt.showturtle()
sqrt.onclick(sqrs)










#clear
def clears(x,y):
    painter.clear()
painter = turtle.Turtle()
painter.speed(9)
screen.onclick(clickers)
pen = turtle.Turtle()
pen.hideturtle()
pen._tracer(1,0)
pen.color("black")
pen.penup()
pen.goto(850, 500)
pen.write("Clear", font=("Super Creamy", 18, "bold"))
clearer = turtle.Turtle(shape = 'circle')
clearer.hideturtle()
clearer._tracer(1,0)
clearer.color("yellow")
clearer.penup()
clearer.goto(930, 516)
clearer.showturtle()
clearer.onclick(clears)

#end fill
def end_fil(x,y):
    painter.end_fill()
    end.color('green')
    time.sleep(0.1)
    end.color('red')
    begin.color('red')
penss = turtle.Turtle()
penss.hideturtle()
penss._tracer(1,0)
penss.color("black")
penss.penup()
penss.goto(400, 500)
penss.write("End Fill", font=("Super Creamy", 18, "bold"))
end = turtle.Turtle(shape = 'circle')
end.hideturtle()
end._tracer(1,0)
end.color("red")
end.penup()
end.goto(500, 516)
end.showturtle()
end.onclick(end_fil)


#begin fill
def beg_fil(x,y):
    painter.begin_fill()
    end.color('red')
    begin.color('green')

pn = turtle.Turtle()
pn.hideturtle()
pn._tracer(1,0)
pn.color("black")
pn.penup()
pn.goto(220, 500)
pn.write("Begin Fill", font=("Super Creamy", 18, "bold"))
begin = turtle.Turtle(shape = 'circle')
begin.hideturtle()
begin._tracer(1,0)
begin.color("red")
begin.penup()
begin.goto(345, 516)
begin.showturtle()
begin.onclick(beg_fil)



#penup
def pensup(x,y):
    painter.penup()
    pendowns.color('red')
    penups.color('green')
pen1 = turtle.Turtle()
pen1.hideturtle()
pen1._tracer(1,0)
pen1.color("black")
pen1.penup()
pen1.goto(720, 500)
pen1.write("PenUp", font=("Super Creamy", 18, "bold"))
penups = turtle.Turtle(shape = 'circle')
penups.hideturtle()
penups._tracer(1,0)
penups.color("red")
penups.penup()
penups.goto(805, 516)
penups.showturtle()
penups.onclick(pensup)


#penup
def pensdown(x,y):
    painter.pendown()
    pendowns.color('green')
    penups.color('red')

pen2 = turtle.Turtle()
pen2.hideturtle()
pen2._tracer(1,0)
pen2.color("black")
pen2.penup()
pen2.goto(550, 500)
pen2.write("PenDown", font=("Super Creamy", 18, "bold"))
pendowns = turtle.Turtle(shape = 'circle')
pendowns.hideturtle()
pendowns._tracer(1,0)
pendowns.color("green")
pendowns.penup()
pendowns.goto(675, 516)
pendowns.showturtle()
pendowns.onclick(pensdown)



#width
pen3 = turtle.Turtle()
pen3.hideturtle()
pen3._tracer(1,0)
pen3.penup()
pen3.goto(-700, 480)
pen3.write("Width:", font=("Super Creamy", 30, "bold"))
pen3.goto(-556, 460)
pen3.write("1", font=("regular", 20, "bold"))
pen3.goto(-506, 460)
pen3.write("2", font=("regular", 20, "bold"))
pen3.goto(-456, 460)
pen3.write("3", font=("regular", 20, "bold"))
pen3.goto(-406, 460)
pen3.write("4", font=("regular", 20, "bold"))
pen3.goto(-356, 460)
pen3.write("5", font=("regular", 20, "bold"))




choser = turtle.Turtle(shape = 'circle')
choser.hideturtle()
choser._tracer(1,0)
choser.color("green")
choser.width(5)
choser.penup()
choser.goto(-550, 502)
choser.showturtle()
line = turtle.Turtle(shape="square")
line.penup()
line.color('green')
line.speed(100)
line.goto(-450, 502)
line.shapesize(stretch_wid=0.5,stretch_len=10)
line.onclick(line_onclick)

def colors_shapes():
    def yellow(x,y):
        painter.color('yellow')
        trt.color('yellow')
        crcs.color('yellow')
        clss.color('yellow')
        squr.color('yellow')
        trg.color('yellow')
    def orange(x,y):
        painter.color('orange')
        trt.color('orange')
        crcs.color('orange')
        clss.color('orange')
        squr.color('orange')
        trg.color('orange')
    def red(x,y):
        painter.color('red')
        trt.color('red')
        crcs.color('red')
        clss.color('red')
        squr.color('red')
        trg.color('red')
    def violet(x,y):
        painter.color('violet')
        trt.color('violet')
        crcs.color('violet')
        clss.color('violet')
        squr.color('violet')
        trg.color('violet')
    def purple(x,y):
        painter.color('purple')
        trt.color('purple')
        crcs.color('purple')
        clss.color('purple')
        squr.color('purple')
        trg.color('purple')
    def blue(x,y):
        painter.color('blue')
        trt.color('blue')
        crcs.color('blue')
        clss.color('blue')
        squr.color('blue')
        trg.color('blue')
    def turquoise(x,y):
        painter.color('turquoise')
        trt.color('turquoise')
        crcs.color('turquoise')
        clss.color('turquoise')
        squr.color('turquoise')
        trg.color('turquoise')
    def light_green(x,y):
        painter.color('lightgreen')
        trt.color('lightgreen')
        crcs.color('lightgreen')
        clss.color('lightgreen')
        squr.color('lightgreen')
        trg.color('lightgreen')
    def green(x,y):
        painter.color('green')
        trt.color('green')
        crcs.color('green')
        clss.color('green')
        squr.color('green')
        trg.color('green')
    def brown(x,y):
        painter.color('brown')
        trt.color('brown')
        crcs.color('brown')
        clss.color('brown')
        squr.color('brown')
        trg.color('brown')
    def black(x,y):
        painter.color('black')
        trt.color('black')
        crcs.color('black')
        clss.color('black')
        squr.color('black')
        trg.color('black')
    def gray(x,y):
        painter.color('gray')
        trt.color('gray')
        crcs.color('gray')
        clss.color('gray')
        squr.color('gray')
        trg.color('gray')
    def white(x,y):
        painter.color('white')
        trt.color('white')
        crcs.color('white')
        clss.color('white')
        squr.color('white')
        trg.color('white')
    def trts(x,y):
        painter.shape('turtle')
    def crc(x,y):
        painter.shape('circle')
    def clas(x,y):
        painter.shape('classic')
    def sqr(x,y):
        painter.shape('square')
    def trng(x,y):
        painter.shape('triangle')
    
    yel = turtle.Turtle(shape='circle')
    yel.color('yellow')
    yel.turtlesize(2)
    yel.penup()
    yel._tracer(1,0)
    yel.goto(-900,500)
    yel.onclick(yellow)
    ora = turtle.Turtle(shape='circle')
    ora.color('orange')
    ora.turtlesize(2)
    ora.penup()
    ora._tracer(1,0)
    ora.goto(-900,440)
    ora.onclick(orange)
    rd = turtle.Turtle(shape='circle')
    rd.color('red')
    rd.turtlesize(2)
    rd.penup()
    rd._tracer(1,0)
    rd.goto(-900,380)
    rd.onclick(red)
    vlt = turtle.Turtle(shape='circle')
    vlt.color('violet')
    vlt.turtlesize(2)
    vlt.penup()
    vlt._tracer(1,0)
    vlt.goto(-900,320)
    vlt.onclick(violet)
    prp = turtle.Turtle(shape='circle')
    prp.color('purple')
    prp.turtlesize(2)
    prp.penup()
    prp._tracer(1,0)
    prp.goto(-900,260)
    prp.onclick(purple)
    blu = turtle.Turtle(shape='circle')
    blu.color('blue')
    blu.turtlesize(2)
    blu.penup()
    blu._tracer(1,0)
    blu.goto(-900,200)
    blu.onclick(blue)
    sk = turtle.Turtle(shape='circle')
    sk.color('turquoise')
    sk.turtlesize(2)
    sk.penup()
    sk._tracer(1,0)
    sk.goto(-900,140)
    sk.onclick(turquoise)
    lg = turtle.Turtle(shape='circle')
    lg.color('light green')
    lg.turtlesize(2)
    lg.penup()
    lg._tracer(1,0)
    lg.goto(-900,80)
    lg.onclick(light_green)
    gr = turtle.Turtle(shape='circle')
    gr.color('green')
    gr.turtlesize(2)
    gr.penup()
    gr._tracer(1,0)
    gr.goto(-900,20)
    gr.onclick(green)
    br = turtle.Turtle(shape='circle')
    br.color('brown')
    br.turtlesize(2)
    br.penup()
    br._tracer(1,0)
    br.goto(-900,-40)
    br.onclick(brown)




    #outline
    blot = turtle.Turtle(shape='circle')
    blot.color('white')
    blot.turtlesize(2.1)
    blot.penup()
    blot._tracer(1,0)
    blot.goto(-900,-100)
    #black
    bl = turtle.Turtle(shape='circle')
    bl.color('black')
    bl.turtlesize(2)
    bl.penup()
    bl._tracer(1,0)
    bl.goto(-900,-100)
    bl.onclick(black)




    gra = turtle.Turtle(shape='circle')
    gra.color('gray')
    gra.turtlesize(2)
    gra.penup()
    gra._tracer(1,0)
    gra.goto(-900,-160)
    gra.onclick(gray)

    
    #outline
    whot = turtle.Turtle(shape='circle')
    whot.color('black')
    whot.turtlesize(2.1)
    whot.penup()
    whot._tracer(1,0)
    whot.goto(-900,-220)
    #white
    wh = turtle.Turtle(shape='circle')
    wh.color('white')
    wh.turtlesize(2)
    wh.penup()
    wh._tracer(1,0)
    wh.goto(-900,-220)
    wh.onclick(white)



    #shapes

    #turtle shape
    trt = turtle.Turtle(shape='turtle')
    trt.turtlesize(2)
    trt._tracer(1,0)
    trt.color(z)
    trt.penup()
    trt.goto(-802,500)
    trt.onclick(trts)

    #circle shape
    crcs = turtle.Turtle(shape='circle')
    crcs.turtlesize(2)
    crcs._tracer(1,0)
    crcs.color(z)
    crcs.penup()
    crcs.goto(-800,440)
    crcs.onclick(crc)

    #classic shape (arrow)
    clss = turtle.Turtle(shape='classic')
    clss.turtlesize(2)
    clss._tracer(1,0)
    clss.color(z)
    clss.penup()
    clss.goto(-795,380)
    clss.onclick(clas)

    #square shape
    squr = turtle.Turtle(shape='square')
    squr.turtlesize(2)
    squr._tracer(1,0)
    squr.color(z)
    squr.penup()
    squr.goto(-802,320)
    squr.onclick(sqr)

    #triangle shape
    trg = turtle.Turtle(shape='triangle')
    trg.turtlesize(2)
    trg.speed(0)
    trg.color(z)
    trg.penup()
    trg.goto(-808,260)
    trg.onclick(trng)




colors_shapes()


    

    
screen.mainloop()
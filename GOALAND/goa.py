import turtle


screen = turtle.Screen()
screen.setup(1920,1080)
# screen.bgpic('text.png')
screen.bgcolor('green')
def G():
    G = 0
    y = 200
    x = -400
    for i in range(18):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        G += 1
    for i in range(22):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 4
        y += 6.5
        G += 1
    y -= 6.5
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 13
        G += 1
    x -= 13
    for i in range(12):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        G += 1
        
    y = 200
    x = -400
    for i in range(16):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        x += 3
        G += 1
    for i in range(15):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 2.5
        x += 6
        G += 1
    x -= 6
    y += 2.5
    for i in range(14):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y +=1
        x += 6
        G += 1
    y -= 1
    x -= 6
    for i in range(19):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y +=10
        G += 1
    y -= 10
    for i in range(19):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 5
        G += 1
    return G
def O():
    O = 0
    y = 200
    x = -120
    for i in range(18):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        O += 1
    y -= 10
    for i in range(21):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 7
        x += 3
        O += 1
    for i in range(21):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        O += 1
    for i in range(21):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y -= 7
        O += 1
    for i in range(18):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        O += 1
    for i in range(15):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        x -=4
        O += 1
    for i in range(21):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 5
        O += 1
    for i in range(17):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        x -= 4.2
        O += 1
    return O
def A():
    A = 0
    y = 40
    x = 130
    for i in range(40):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 12
        x +=2.8
        A += 1
    for i in range(41):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 12
        x +=2.8
        A += 1
    x = 170
    y = 200
    for i in range(25):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 6 
        A += 1
    return A
def s():
    s = 0
    x = -940
    y = 150
    for i in range(40):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10 
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        x += 6 
        s += 1
    y += 10
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 6 
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        x += 4
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        x -=5
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        x +=5
        s += 1
    return s
def Aa():
    a = 0
    x = -670
    y = 10
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10 
        a += 1
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        x += 7 
        a += 1
    x -= 7
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        a += 1
    y += 10
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        x -= 7
        a += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 13
        a += 1
    x += 13
    for i in range(7):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 13
        x -= 5
        a += 1
    y -= 13
    x += 5
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 13
        x += 5
        a += 1
    return a
def u():
    u = 0
    x = -560
    y = 0
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -=2
        y -= 10 
        u += 1
    for i in range(7):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        y -= 10 
        u += 1
    y += 10
    for i in range(7):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 7
        y += 10 
        u += 1
    x -= 7
    y -= 10
    for i in range(7):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 4
        y += 10 
        u += 1
    y -= 10
    x += 4
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        y -= 10 
        u += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10 
        u += 1
    x = -436
    y = -42
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10 
        x += 7
        u += 1
    y -= 10
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10 
        x += 7
        u += 1
    for i in range(25):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10 
        u += 1
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10 
        x -= 4
        u += 1
    y += 10
    x += 4
    for i in range(4):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 5 
        x -= 12
        u += 1
    
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 10
        u += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 5
        y += 8 
        u += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8 
        u += 1
    for i in range(4):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        x += 7 
        u += 1
    return u

def k():
    k = 0
    x = -290
    y = -242
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        x -= 6
        k += 1
    for i in range(7):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        k += 1
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        x += 5
        k += 1
    y += 8
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 6
        k += 1
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 6
        y += 5
        k += 1
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        k += 1
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 5
        y += 4
        k += 1
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        y += 4
        k += 1
    y -= 4
    x -= 5
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        k += 1
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 2
        x -= 3
        k += 1
    return k
def e():
    e = 0
    x = -100
    y = -115
    for i in range(9):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        e += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        x += 5
        e += 1
    y -= 8
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        e += 1
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y -= 5
        e += 1
    for i in range(34):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        e += 1
    y += 8
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        x -= 2
        e += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 5
        x -= 5
        e += 1
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 5
        x -= 5
        e += 1
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        e += 1
    x += 6
    for i in range(7):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y += 8
        e += 1
    return e

def t():
    t = 0
    x = 70
    y = -155
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        t += 1  
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        y += 8
        t += 1  
    y -= 8
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        t += 1  
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y -= 5
        t += 1 
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 4
        y += 5
        t += 1  
    y -= 4
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 4
        t += 1  
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y -= 4
        t += 1  
    y += 4
    x -= 2
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 1
        y -= 4
        t += 1  
    for i in range(17):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 4
        t += 1  
    for i in range(23):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 1.3
        y -= 4
        t += 1  
    x = 200
    y = -45
    for i in range(28):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 4
        t += 1  
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 6
        x -= 1
        t += 1  
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 2
        x -= 4
        t += 1  
    for i in range(13):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 2
        x -= 4
        t += 1  
    for i in range(15):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 5
        x -= 1.6
        t += 1  
    return t
def E():
    e = 0
    x = 365
    y = -115
    for i in range(9):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        e += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        x += 5
        e += 1
    y -= 8
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        e += 1
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y -= 5
        e += 1
    for i in range(34):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        e += 1
    y += 8
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        x -= 2
        e += 1
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 5
        x -= 5
        e += 1
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 5
        x -= 5
        e += 1
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        e += 1
    x += 6
    for i in range(7):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y += 8
        e += 1
    return e
def S():
    s = 0
    x = 515
    y = 150
    for i in range(40):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10 
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 10
        x += 6 
        s += 1
    y += 10
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 6 
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        x += 4
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        x -=5
        s += 1
    for i in range(6):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 10
        x +=5
        s += 1
    return s

def o():
    o = 0
    x = 670
    y = -272
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        y -= 8
        o += 1  
    x = 670
    y = -272
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y += 8
        o += 1  
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        y += 8
        o += 1  
    y -= 8
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        o += 1  
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 3
        y -= 5
        o += 1 
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 4
        y += 5
        o += 1  
    y -= 4
    for i in range(8):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 4
        o += 1  
    for i in range(10):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x += 5
        y -= 8
        o += 1  
    for i in range(11):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        y -= 8
        o += 1  
    for i in range(5):
        T = turtle.Turtle(shape='turtle')
        T.color('black')
        T._tracer(30,0)
        T.penup()
        T.setpos(x,y)
        x -= 5
        y -= 8
        o += 1  
    return o









def paint_count():
    G1 = G()
    O1 = O()
    A1 = A()
    s1 = s()
    a1 = Aa()
    u1 = u()
    k1 = k()
    e1 = e()
    t1 = t()
    e2 = E()
    s2 = S()
    o1 = o()
    # a2 = A2()
    return G1 + O1 + A1 + s1 + a1*2 + u1 + k1 + e1 + t1 + e2 + s2 + o1
z = paint_count()
def sums():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("black")
    pen.penup()
    pen.setpos(-800, 200)
    pen.write(f"Total turtles: {z}", font=("regular", 20, "bold"))
sums()
    
    
screen.exitonclick()
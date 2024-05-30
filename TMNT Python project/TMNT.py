import turtle
import time
import random
import pygame

pygame.mixer.init()
pygame.mixer.music.set_volume(0.1)
intro = input("""Hello, this TMNT Racing.You start by entering 
which turtle will win and how much you want to bid on that turtle.
If your choosen turtle won you win money.
If you are ready Enter "Ready" and game will start😄: """)
if intro.lower() == "ready":
    WIDTH, HEIGHT = 500,500
    turtles_dict = {
        "donatello" : "purple",
        "raphael" : "red",
        "michelangelo" : "orange",
        "leonardo" : "blue"
    }
    colors = ["donatello","raphael","michelangelo","leonardo"]
    def race(colors):
        racers = create_turtles(colors)
        racers[0].onclick(onclick_don)
        racers[1].onclick(onclick_raph)
        racers[2].onclick(onclick_mich)
        racers[3].onclick(onclick_leo)
        while True:
            for i in racers:
                i.forward(random.randrange(1,20))

                x,y = i.pos()
                if y >= HEIGHT // 2 - 5:
                    return colors[racers.index(i)]
    def create_turtles(colors):
        racers = []
        spacing = WIDTH // (len(colors) + 1)
        music()
        for i, color in enumerate(colors):
            racer = turtle.Turtle()
            racer.speed(2)
            racer.color(turtles_dict[color])
            racer.shape("turtle")
            racer.left(90)
            text(color)
            time.sleep(1.5)
            racer.penup()
            racer.setpos(-WIDTH // 2 + (i + 1) * spacing, -HEIGHT// 2 + 20)
            racer.pendown()
            racer.speed(1)
            racers.append(racer)
        return racers
    def turtle_screen():
        screen = turtle.Screen()
        screen.setup(WIDTH,HEIGHT)
        screen.bgpic("background.png")
        screen.title("TMNT Race")

    def Color():
        choosen_color = input(f"Which turtle do you think will win from {", ".join(colors)}: ")
        while True:
            if choosen_color in colors:
                break
            else:
                choosen_color = input(f"Choose a turtle from this list! {", ".join(colors)}: ")
        return choosen_color
    def bids():
        bid = input(f"How many dollars you want to bid on {y} turtle. Minimum amount of money to bid is 10$ and maximum 10 000$: ")
        while True:
            if bid.isnumeric():
                if int(bid) < 10 or int(bid) > 10000:
                    bid = input("Try again. Minimum amount of money to bid is 10$ and maximum 10 000$: ")
                else:
                    return int(bid) 
            else:
                bid = input("Try again. You should enter how many dollars you want to bid in numeric value: ")
    y = Color()
    z = bids()
    turtle_screen()
    def onclick_leo(x,y):
        pygame.mixer.music.load('leonardo.mp3')
        pygame.mixer.music.play()
    def onclick_mich(x,y):
        pygame.mixer.music.load('michelangelo.mp3')
        pygame.mixer.music.play()
    def onclick_raph(x,y):
        pygame.mixer.music.load('raphael.mp3')
        pygame.mixer.music.play()
    def onclick_don(x,y):
        pygame.mixer.music.load('donatello.mp3')
        pygame.mixer.music.play()
    
    

    def music():
        pygame.mixer.music.load("0514.MP3")
        pygame.mixer.music.play()

    def text(turtle_name):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0, 50)
        t.color(turtles_dict[turtle_name])
        font_name = "b Balik Awan"
        font_size = 30
        font_style = "normal"
        font = (font_name, font_size, font_style)
        t.write(turtle_name, align="center", font=font)
        def disappear():
            t.clear()
        turtle.ontimer(disappear, 2100)
    
    winner = race(colors)
    if winner == y:
        x = z * 4
        print(f"Congrulations!🎆 Your chosen {y} won the race and you won {x}$.")
    else:
        print(f"Your chosen {y} lost😥, {winner} won and you lost {z}$.")
    pygame.mixer.music.load("win_" + winner+ '.mp3')
    pygame.mixer.music.play()
    time.sleep(5)   
else:
    print("Try again when you will be ready🙂")
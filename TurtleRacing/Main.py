import turtle
import time
import random
intro = input("""Hello, this Turtle Racing.You start by entering how many turtles will race
which color turtle will win and how much you want to bid on that turtle.If your choosen turtle
won you win money,but it depends on number of turtles in the race.
If you are ready Enter "Ready" and game will start😄: """)
if intro.lower() == "ready":
    WIDTH, HEIGHT = 500,500
    colors = ["red","green","blue","black","cyan","purple","yellow","pink","light blue","orange"]
    def turtle_number():
        turtles = 0
        while True:
            turtles = input("Enter how many turtles you want to race between 2 and 10: ")
            if turtles.isdigit():    
                turtles = int(turtles)
            else:
                print("Your input is not numeric... Try Again!")
                continue
            if turtles >= 2 and turtles <=10:
                return turtles
            else:
                print("Number not in range 2-10. Try Again !")
    def race(color):
        racers = create_turtles(color)
        while True:
            for i in racers:
                i.forward(random.randrange(1,20))

                x,y = i.pos()
                if y >= HEIGHT // 2 - 5:
                    return color[racers.index(i)]
    def create_turtles(color):
        racers = []
        spacing = WIDTH // (len(color) + 1)
        for i, color in enumerate(color):
            racer = turtle.Turtle()
            racer.speed(2)
            racer.color(color)
            racer.shape("turtle")
            racer.left(90)
            racer.penup()
            racer.setpos(-WIDTH // 2 + (i + 1) * spacing, -HEIGHT// 2 + 20)
            racer.pendown()
            racer.speed(1)
            racers.append(racer)

        return racers
    def turtle_screen():
        screen = turtle.Screen()
        screen.setup(WIDTH,HEIGHT)
        screen.title("Turtle Race")
    turtles = turtle_number()

    random.shuffle(colors)
    color = colors[:turtles]
    def Color():
        choosen_color = input(f"Which color turtle do you think will win from {", ".join(color)}: ")
        while True:
            if choosen_color in color:
                break
            else:
                choosen_color = input(f"Choose a color from this list! {", ".join(color)}: ")
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
    winner = race(color)
    if winner == y:
        x = 0
        if turtle_number() == 2:
            x = z * 1.2
        elif turtle_number() == 3:
            x = z * 1.3 
        elif turtle_number() == 4:
            x = z * 1.4
        elif turtle_number() == 5:
            x = z * 1.5
        elif turtle_number() == 6:
            x = z * 1.6
        elif turtle_number() == 7:
            x = z * 1.7
        elif turtle_number() == 8:
            x = z * 1.8
        elif turtle_number() == 9:
            x = z * 1.9
        elif turtle_number() == 10:
            x = z * 2
        
        print(f"Congrulations! Your chosen {y} turtle won the race and you won {x}$.")
    else:
        print(f"Your chosen {y} lost😥, {winner} turtle won and you lost {z}$.")
    time.sleep(5)   
else:
    print("Try again when you will be ready🙂")
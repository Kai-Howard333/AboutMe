#imports
import turtle as t
import random
import time

#game configuration
delay = 0.08
sizeOfHead = 1
score = 0
score1 = 0
score2 = 0

computerBodyList = []
movementAmount = 20

#object creation
#TODO 2: create your turtles
#window
wn = t.Screen()
wn.setup(width = 600,height = 600)

#function & command development
#TODO 3: create basic movement for the head (up, down,left, right)


def solo():
    global delay
    score = 0
    listOfThyBody = []

    #snake head
    head = t.Turtle()
    head.shape("square")
    head.shapesize(sizeOfHead)
    head.color("green")
    head.direction = "stop"
    head.penup()

    #snake food
    food = t.Turtle()
    food.shape("turtle")
    food.color("saddle brown")
    food.speed(0)
    food.penup()
    food.goto(100,100)

    #scorekeeper
    scorekeeper = t.Turtle()
    scorekeeper.ht()
    scorekeeper.speed(0)
    scorekeeper.penup()
    scorekeeper.goto(230,230)
    scoreFont = ("Comic Sans MS",16,"normal")
    scorekeeper.write("Score: 0",align = "center",font = scoreFont)

    #function & command development
    #TODO 3: create basic movement for the head (up, down,left, right)
    def up1():
        #if head is going down, we can't go up
        if head.direction != "down":
            head.direction = "up"
    def down1():
        if head.direction != "up":
            head.direction = "down"
    def left1():
        if head.direction != "right":
            head.direction = "left"
    def right1():
        if head.direction != "left":
            head.direction = "right"

    def move():
        global movementAmount
        if head.direction == "up":      #moves the snake up
            head.sety(head.ycor() + movementAmount)
        elif head.direction == "down":  #moves the snake down
            head.sety(head.ycor() - movementAmount)
        elif head.direction == "left":  #moves the snake left
            head.setx(head.xcor() - movementAmount)
        elif head.direction == "right": #moves the snake right
            head.setx(head.xcor() + movementAmount)
        else:
            head.goto(0,0)
    def die():
        global movementAmount, score, delay
        # movementAmount = 20
        delay = 0.08
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        score = 0
        scorekeeper.clear()
        scorekeeper.write(("Score: "+str(score)),align = "center",font = scoreFont)
        #player
        for bp in listOfThyBody:
            bp.goto(random.randint(500,1000),random.randint(500,1000))
        listOfThyBody.clear()



    #connect key bindings
    wn.listen()
    wn.onkeypress(up1,"w")
    wn.onkeypress(down1,"s")
    wn.onkeypress(left1,"a")
    wn.onkeypress(right1,"d")

    #game play
    #TODO 6: while the game plays, move the snake (may need to check on slowing down the movement)
    while True:

        #check for boundary collision
        if (head.xcor() < (-300 + sizeOfHead/2) or head.xcor() > (300 - sizeOfHead/2)) or (head.ycor() < (-300 + sizeOfHead/2) or head.ycor() > (300 - sizeOfHead/2)):
            die()

        #check for collision with the food
        #  object.distance(object 2)
        if head.distance(food) < 20:
            # movementAmount += 2       #screws up the movement
            delay = delay / 2
            score += 1
            # print("Score: {}".format(score))
            scorekeeper.clear()
            scorekeeper.write(("Score: "+str(score)),align = "center",font = scoreFont)
            x,y = random.randint(-280,280), random.randint(-280,280)
            food.penup()
            food.goto(x,y)
            food.pendown()

            newBodyPart = t.Turtle()
            newBodyPart.ht()
            newBodyPart.shape("square")
            newBodyPart.shapesize(sizeOfHead)
            newBodyPart.color("green")
            newBodyPart.penup()
            newBodyPart.goto(score*10,0)
            newBodyPart.st()
            newBodyPart.speed(0)
            listOfThyBody.append(newBodyPart)

        #moving the body parts and chek to see if the head hit it
        #iterate through the list
        for index in range(len(listOfThyBody)-1,0,-1):
            #grab the x,y coordinate of the turtle
            x = listOfThyBody[index-1].xcor()
            y = listOfThyBody[index-1].ycor()
            #reset the x,y coordinate of the next turtle
            listOfThyBody[index].goto(x,y)
            # listOfThyBody[index].goto(listOfThyBody[index-1].xcor(),listOfThyBody[index-1].ycor())
            if head.distance(listOfThyBody[index]) < 20:
                die()
                break

        #Move the neck of bodypart[0] to where the head is
        if len(listOfThyBody)>0:
            listOfThyBody[0].goto(head.xcor(),head.ycor())
            x = head.xcor()
            y = head.ycor()
            listOfThyBody[0].goto(x,y)

        #moving the
        move()

        #sleep so Bander can keep up with the game
        time.sleep(delay)

def pvp():
    global delay, score1, score2
    listOfThyBody1 = []
    listOfThyBody2 = []
    
    #Player 1 snake head
    head1 = t.Turtle()
    head1.shape("square")
    head1.shapesize(sizeOfHead)
    head1.color("green")
    head1.penup()
    head1.goto(50,0)
    head1.direction = "stop"

    #Player 2 snake head
    head2 = t.Turtle()
    head2.shape("square")
    head2.shapesize(sizeOfHead)
    head2.color("green")
    head2.penup()
    head2.goto(-50,0)
    head2.direction = "stop"

    #snake food
    food = t.Turtle()
    food.shape("turtle")
    food.color("saddle brown")
    food.speed(0)
    food.penup()
    food.goto(100,100)

    #scorekeeper
    scorekeeper1 = t.Turtle()
    scorekeeper1.ht()
    scorekeeper1.speed(0)
    scorekeeper1.penup()
    scorekeeper1.goto(230,230)
    scoreFont = ("Comic Sans MS",16,"normal")
    scorekeeper1.write("Score: 0",align = "center",font = scoreFont)
    
    scorekeeper2 = t.Turtle()
    scorekeeper2.ht()
    scorekeeper2.speed(0)
    scorekeeper2.penup()
    scorekeeper2.goto(-230,230)
    scoreFont = ("Comic Sans MS",16,"normal")
    scorekeeper2.write("Score: 0",align = "center",font = scoreFont)

    #function & command development
    #TODO 3: create basic movement for the head (up, down,left, right)
    def up1():
        #if head is going down, we can't go up
        if head1.direction != "down":
            head1.direction = "up"
    def down1():
        if head1.direction != "up":
            head1.direction = "down"
    def left1():
        if head1.direction != "right":
            head1.direction = "left"
    def right1():
        if head1.direction != "left":
            head1.direction = "right"

    #player 2
    def up2():
        #if head2 is going down, we can't go up
        if head2.direction != "down":
            head2.direction = "up"
    def down2():
        if head2.direction != "up":
            head2.direction = "down"
    def left2():
        if head2.direction != "right":
            head2.direction = "left"
    def right2():
        if head2.direction != "left":
            head2.direction = "right"

    def move1():
        global movementAmount
        if head1.direction == "up":      #moves the snake up
            head1.sety(head1.ycor() + movementAmount)
        elif head1.direction == "down":  #moves the snake down
            head1.sety(head1.ycor() - movementAmount)
        elif head1.direction == "left":  #moves the snake left
            head1.setx(head1.xcor() - movementAmount)
        elif head1.direction == "right": #moves the snake right
            head1.setx(head1.xcor() + movementAmount)
        else:
            head1.goto(0,0)
    
    def move2():
        global movementAmount
        if head2.direction == "up":      #moves the snake up
            head2.sety(head2.ycor() + movementAmount)
        elif head2.direction == "down":  #moves the snake down
            head2.sety(head2.ycor() - movementAmount)
        elif head2.direction == "left":  #moves the snake left
            head2.setx(head2.xcor() - movementAmount)
        elif head2.direction == "right": #moves the snake right
            head2.setx(head2.xcor() + movementAmount)
        else:
            head2.goto(0,0)
        
    def die():
        global score1, score2, movementAmount
        # movementAmount = 20
        delay = 0.08
        time.sleep(1)
        head1.goto(50,0)
        head2.goto(-50,0)
        head1.direction = "stop"
        head2.direction = "stop"
        score1 = 0
        score2 = 0
        scorekeeper1.clear()
        scorekeeper1.write(("Score: "+str(score1)),align = "center",font = scoreFont)
        scorekeeper2.clear()
        scorekeeper2.write(("Score: "+str(score2)),align = "center",font = scoreFont)
        #player1
        for bp in listOfThyBody1:
            bp.goto(random.randint(500,1000),random.randint(500,1000))
        listOfThyBody1.clear()
        #player2
        for bp in listOfThyBody2:
            bp.goto(random.randint(500,1000),random.randint(500,1000))
        listOfThyBody2.clear()

    #connect key bindings
    wn.listen()
    wn.onkeypress(up1,"w")
    wn.onkeypress(down1,"s")
    wn.onkeypress(left1,"a")
    wn.onkeypress(right1,"d")

    wn.onkeypress(up2,"Up")
    wn.onkeypress(down2,"Down")
    wn.onkeypress(left2,"Left")
    wn.onkeypress(right2,"Right")

    #game play
    #TODO 6: while the game plays, move the snake (may need to check on slowing down the movement)
    while True:

        #check for boundary collision
        if (head1.xcor() < (-300 + sizeOfHead/2) or head1.xcor() > (300 - sizeOfHead/2)) or (head1.ycor() < (-300 + sizeOfHead/2) or head1.ycor() > (300 - sizeOfHead/2)):
            die()
        elif (head2.xcor() < (-300 + sizeOfHead/2) or head2.xcor() > (300 - sizeOfHead/2)) or (head2.ycor() < (-300 + sizeOfHead/2) or head2.ycor() > (300 - sizeOfHead/2)):
            die()

        #check for collision with the food
        #  object.distance(object 2)
        if head1.distance(food) < 20:
            # movementAmount += 2       #screws up the movement
            score1 += 1
            # print("Score: {}".format(score))
            scorekeeper1.clear()
            scorekeeper1.write(("Score: "+str(score1)),align = "center",font = scoreFont)
            x,y = random.randint(-280,280), random.randint(-280,280)
            food.penup()
            food.goto(x,y)
            food.pendown()

            newBodyPart1 = t.Turtle()
            newBodyPart1.ht()
            newBodyPart1.shape("square")
            newBodyPart1.shapesize(sizeOfHead)
            newBodyPart1.color("green")
            newBodyPart1.penup()
            newBodyPart1.goto(score*10,0)
            newBodyPart1.st()
            newBodyPart1.speed(0)
            listOfThyBody1.append(newBodyPart1)

        elif head2.distance(food) < 20:
            # movementAmount += 2       #screws up the movement
            score2 += 1
            # print("Score: {}".format(score))
            scorekeeper2.clear()
            scorekeeper2.write(("Score: "+str(score2)),align = "center",font = scoreFont)
            x,y = random.randint(-280,280), random.randint(-280,280)
            food.penup()
            food.goto(x,y)
            food.pendown()

            newBodyPart2 = t.Turtle()
            newBodyPart2.ht()
            newBodyPart2.shape("square")
            newBodyPart2.shapesize(sizeOfHead)
            newBodyPart2.color("green")
            newBodyPart2.penup()
            newBodyPart2.goto(score*10,0)
            newBodyPart2.st()
            newBodyPart2.speed(0)
            listOfThyBody2.append(newBodyPart2)

        #moving the body parts and chek to see if the head hit it
        #iterate through the list
        for index in range(len(listOfThyBody1)-1,0,-1):
            #grab the x,y coordinate of the turtle
            x = listOfThyBody1[index-1].xcor()
            y = listOfThyBody1[index-1].ycor()
            #reset the x,y coordinate of the next turtle
            listOfThyBody1[index].goto(x,y)
            # listOfThyBody[index].goto(listOfThyBody[index-1].xcor(),listOfThyBody[index-1].ycor())
            if head1.distance(listOfThyBody1[index]) < 20:
                die()
                break
        #player 2
        for index in range(len(listOfThyBody2)-1,0,-1):
            #grab the x,y coordinate of the turtle
            x = listOfThyBody2[index-1].xcor()
            y = listOfThyBody2[index-1].ycor()
            #reset the x,y coordinate of the next turtle
            listOfThyBody2[index].goto(x,y)
            if head2.distance(listOfThyBody2[index]) < 20:
                die()
                break

        #Move the neck of bodypart[0] to where the head is
        if len(listOfThyBody1)>0:
            listOfThyBody1[0].goto(head1.xcor(),head1.ycor())
            x = head1.xcor()
            y = head1.ycor()
            listOfThyBody1[0].goto(x,y)
        #player 2
        if len(listOfThyBody2)>0:
            listOfThyBody2[0].goto(head2.xcor(),head2.ycor())
            x = head2.xcor()
            y = head2.ycor()
            listOfThyBody2[0].goto(x,y)

        #moving the
        move1()
        move2()

        #sleep so Bander can keep up with the game
        time.sleep(delay)

def ai():
    global delay, computerBodyList, score
    #computer snake head
    computerHead = t.Turtle("square", visible= 1)
    computerHead.shape("square")
    computerHead.shapesize(sizeOfHead)
    computerHead.color("blue")
    computerHead.direction = "stop"
    computerHead.penup()
    #snake food
    food = t.Turtle()
    food.shape("turtle")
    food.color("saddle brown")
    food.speed(0)
    food.penup()
    food.goto(100,100)
    
    def computerDie():
        computerHead.goto(50,0)
        computerHead.direction = "stop"
        score = 0
        #computer
        for bp in computerBodyList:
            bp.goto(random.randint(500,1000),random.randint(500,1000))
        computerBodyList.clear()

    def autonomous():
        # global computerBodyList
        while True:
            if computerHead.xcor() > food.xcor():
                computerHead.setheading(180)
            elif computerHead.xcor() < food.xcor():
                computerHead.setheading(0)
            elif computerHead.xcor() == food.xcor():
                if computerHead.ycor() > food.ycor():
                    computerHead.setheading(270)
                elif computerHead.ycor() < food.ycor():
                    computerHead.setheading(90)
            computerHead.fd(20)
    

    while True:
        #check for collision with the food
        #  object.distance(object 2)
        if computerHead.distance(food) < 20:
            delay = delay / 2
            score += 1
            x,y = random.randint(-280,280), random.randint(-280,280)
            food.penup()
            food.goto(x,y)
            food.pendown()

            newBodyPart = t.Turtle()
            newBodyPart.ht()
            newBodyPart.shape("square")
            newBodyPart.shapesize(sizeOfHead)
            newBodyPart.color("green")
            newBodyPart.penup()
            newBodyPart.goto(score*10,0)
            newBodyPart.st()
            newBodyPart.speed(0)
            computerBodyList.append(newBodyPart)

        #moving the body parts and chek to see if the computerHead hit it
        #iterate through the list
        for index in range(len(computerBodyList)-1,0,-1):
            #grab the x,y coordinate of the turtle
            x = computerBodyList[index-1].xcor()
            y = computerBodyList[index-1].ycor()
            #reset the x,y coordinate of the next turtle
            computerBodyList[index].goto(x,y)
            # computerBodyList[index].goto(computerBodyList[index-1].xcor(),computerBodyList[index-1].ycor())
            if computerHead.distance(computerBodyList[index]) < 20:
                computerDie()
                break

        #Move the neck of bodypart[0] to where the computerHead is
        if len(computerBodyList)>0:
            computerBodyList[0].goto(computerHead.xcor(),computerHead.ycor())
            x = computerHead.xcor()
            y = computerHead.ycor()
            computerBodyList[0].goto(x,y)

        #moving the
        autonomous()

        #sleep so Bander can keep up with the game
        time.sleep(delay)

    # if score > 20:
    #     computerDie()
        

def pvc():
    global delay, computerBodyList, score
    score = 0
    listOfThyBody = []

    #snake head
    head = t.Turtle()
    head.shape("square")
    head.shapesize(sizeOfHead)
    head.color("green")
    head.direction = "stop"
    head.penup()

    #computer snake head
    computerHead = t.Turtle("square", visible= 1)
    computerHead.shape("square")
    computerHead.shapesize(sizeOfHead)
    computerHead.color("blue")
    computerHead.direction = "stop"
    computerHead.penup()

    #snake food
    food = t.Turtle()
    food.shape("turtle")
    food.color("saddle brown")
    food.speed(0)
    food.penup()
    food.goto(100,100)

    #scorekeeper
    scorekeeper = t.Turtle()
    scorekeeper.ht()
    scorekeeper.speed(0)
    scorekeeper.penup()
    scorekeeper.goto(230,230)
    scoreFont = ("Comic Sans MS",16,"normal")
    scorekeeper.write("Score: 0",align = "center",font = scoreFont)

    def computerDie():
        computerHead.goto(50,0)
        computerHead.direction = "stop"
        score = 0
        #computer
        for bp in computerBodyList:
            bp.goto(random.randint(500,1000),random.randint(500,1000))
        computerBodyList.clear()
    
    def autonomous():
        # global computerBodyList
        while True:
            if computerHead.xcor() > food.xcor():
                computerHead.setheading(180)
            elif computerHead.xcor() < food.xcor():
                computerHead.setheading(0)
            elif computerHead.xcor() == food.xcor():
                if computerHead.ycor() > food.ycor():
                    computerHead.setheading(270)
                elif computerHead.ycor() < food.ycor():
                    computerHead.setheading(90)
            computerHead.fd(20)

    while True:
        #check for collision with the food
        #  object.distance(object 2)
        if computerHead.distance(food) < 20:
            delay = delay / 2
            score += 1
            x,y = random.randint(-280,280), random.randint(-280,280)
            food.penup()
            food.goto(x,y)
            food.pendown()

            newBodyPart = t.Turtle()
            newBodyPart.ht()
            newBodyPart.shape("square")
            newBodyPart.shapesize(sizeOfHead)
            newBodyPart.color("green")
            newBodyPart.penup()
            newBodyPart.goto(score*10,0)
            newBodyPart.st()
            newBodyPart.speed(0)
            computerBodyList.append(newBodyPart)

        #moving the body parts and chek to see if the computerHead hit it
        #iterate through the list
        for index in range(len(computerBodyList)-1,0,-1):
            #grab the x,y coordinate of the turtle
            x = computerBodyList[index-1].xcor()
            y = computerBodyList[index-1].ycor()
            #reset the x,y coordinate of the next turtle
            computerBodyList[index].goto(x,y)
            # computerBodyList[index].goto(computerBodyList[index-1].xcor(),computerBodyList[index-1].ycor())
            if computerHead.distance(computerBodyList[index]) < 20:
                computerDie()
                break

        #Move the neck of bodypart[0] to where the computerHead is
        if len(computerBodyList)>0:
            computerBodyList[0].goto(computerHead.xcor(),computerHead.ycor())
            x = computerHead.xcor()
            y = computerHead.ycor()
            computerBodyList[0].goto(x,y)

        #moving the
        autonomous()

    def up1():
        #if head is going down, we can't go up
        if head.direction != "down":
            head.direction = "up"
    def down1():
        if head.direction != "up":
            head.direction = "down"
    def left1():
        if head.direction != "right":
            head.direction = "left"
    def right1():
        if head.direction != "left":
            head.direction = "right"

    def move():
        global movementAmount
        if head.direction == "up":      #moves the snake up
            head.sety(head.ycor() + movementAmount)
        elif head.direction == "down":  #moves the snake down
            head.sety(head.ycor() - movementAmount)
        elif head.direction == "left":  #moves the snake left
            head.setx(head.xcor() - movementAmount)
        elif head.direction == "right": #moves the snake right
            head.setx(head.xcor() + movementAmount)
        else:
            head.goto(0,0)
    def die():
        global movementAmount, score
        # movementAmount = 20
        delay = 0.08
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        score = 0
        scorekeeper.clear()
        scorekeeper.write(("Score: "+str(score)),align = "center",font = scoreFont)
        #player
        for bp in listOfThyBody:
            bp.goto(random.randint(500,1000),random.randint(500,1000))
        listOfThyBody.clear()



    #connect key bindings
    wn.listen()
    wn.onkeypress(up1,"w")
    wn.onkeypress(down1,"s")
    wn.onkeypress(left1,"a")
    wn.onkeypress(right1,"d")

    #game play
    #TODO 6: while the game plays, move the snake (may need to check on slowing down the movement)
    while True:

        #check for boundary collision
        if (head.xcor() < (-300 + sizeOfHead/2) or head.xcor() > (300 - sizeOfHead/2)) or (head.ycor() < (-300 + sizeOfHead/2) or head.ycor() > (300 - sizeOfHead/2)):
            die()

        #check for collision with the food
        #  object.distance(object 2)
        if head.distance(food) < 20:
            # movementAmount += 2       #screws up the movement
            delay = delay / 2
            score += 1
            # print("Score: {}".format(score))
            scorekeeper.clear()
            scorekeeper.write(("Score: "+str(score)),align = "center",font = scoreFont)
            x,y = random.randint(-280,280), random.randint(-280,280)
            food.penup()
            food.goto(x,y)
            food.pendown()

            newBodyPart = t.Turtle()
            newBodyPart.ht()
            newBodyPart.shape("square")
            newBodyPart.shapesize(sizeOfHead)
            newBodyPart.color("green")
            newBodyPart.penup()
            newBodyPart.goto(score*10,0)
            newBodyPart.st()
            newBodyPart.speed(0)
            listOfThyBody.append(newBodyPart)

        #moving the body parts and chek to see if the head hit it
        #iterate through the list
        for index in range(len(listOfThyBody)-1,0,-1):
            #grab the x,y coordinate of the turtle
            x = listOfThyBody[index-1].xcor()
            y = listOfThyBody[index-1].ycor()
            #reset the x,y coordinate of the next turtle
            listOfThyBody[index].goto(x,y)
            # listOfThyBody[index].goto(listOfThyBody[index-1].xcor(),listOfThyBody[index-1].ycor())
            if head.distance(listOfThyBody[index]) < 20:
                die()
                break

        #Move the neck of bodypart[0] to where the head is
        if len(listOfThyBody)>0:
            listOfThyBody[0].goto(head.xcor(),head.ycor())
            x = head.xcor()
            y = head.ycor()
            listOfThyBody[0].goto(x,y)

        #moving the snake
        move()

        time.sleep(delay)

def keys():
    #connect key bindings
    wn.listen()
    wn.onkeypress(solo,"1")
    wn.onkeypress(pvp,"2")
    wn.onkeypress(ai,"3")
    wn.onkeypress(pvc,"4")
keys()
wn.mainloop()

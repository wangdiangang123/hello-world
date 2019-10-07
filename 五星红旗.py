import turtle

turtle.setup(650,650,200,200)

turtle.begin_fill()

turtle.fillcolor("red")

turtle.pendown()

turtle.fd(300)

turtle.seth(90)

turtle.fd(200)

turtle.seth(180)

turtle.fd(300)

turtle.seth(270)

turtle.fd(200)

turtle.end_fill()

turtle.penup()

turtle.seth(0)

turtle.fd(21)

turtle.seth(90)

turtle.fd(160)

turtle.pencolor("yellow")

turtle.begin_fill()

turtle.fillcolor("yellow")

turtle.pd()

turtle.seth(0)

turtle.fd(25)

turtle.seth(72)

turtle.fd(25)

turtle.seth(-72)

turtle.fd(25)

turtle.seth(0)

turtle.fd(25)

turtle.seth(-146)

turtle.fd(25)

turtle.seth(-72)

turtle.fd(25)

turtle.seth(146)

turtle.fd(25)

turtle.seth(-146)

turtle.fd(25)

turtle.seth(72)

turtle.fd(25)

turtle.seth(146)

turtle.fd(25)

turtle.end_fill()

turtle.pu()

turtle.goto(92,184)

turtle.hideturtle()

turtle.pencolor("yellow")

turtle.begin_fill()

turtle.fillcolor("yellow")

turtle.pd()

turtle.setheading(305)

turtle.down()

for i in range (5):    

    turtle.forward(20)

    turtle.left(144)

turtle.end_fill()

turtle.begin_fill()

turtle.up()

turtle.goto(112,158)

turtle.setheading(30)

turtle.down()

for i in range (5):  

    turtle.forward(20)

    turtle.right(144)

turtle.end_fill()

turtle.begin_fill()

turtle.up()

turtle.goto(112,133)

turtle.setheading(5)

turtle.down()

for i in range (5):   

    turtle.forward(20)

    turtle.right(144)



turtle.end_fill()

turtle.begin_fill()

turtle.up()

turtle.goto(93,116)

turtle.setheading(300)

turtle.down()

for i in range (5):  

    turtle.forward(20)

    turtle.left(144)



turtle.end_fill()

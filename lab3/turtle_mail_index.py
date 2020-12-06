import turtle as t


def turtle_one():
    t.penup()
    t.forward(30)
    t.pendown()
    t.left(90+30)


def transition():
    if i == zero:
        t.penup()
        t.left(180)
        t.forward(100)
        t.pendown()
        t.left(270)
    else:
        t.left(180)
        t.penup()
        t.forward(120)
        t.right(90)
        t.forward(20)
        if i == seven_number:
            t.forward(40)
        t.left(270)
        t.pendown()


t.shape('turtle')
t.speed(4)
t.width(3)
t.color('blue')
x_constanta = 60

t.penup()
t.goto(-200,0)
t.left(-90)
t.pendown()

one = [t.forward, t.right, t.right, t.forward, t.forward]
four = [t.forward, t.left, t.forward, t.left, t.forward, t.right, t.right,
        t.right, t.forward, t.forward]
seven_number = [t.left, t.forward, t.right, t.right,
                t.forward, t.left, t.forward]
zero = [t.right, t.forward, t.forward, t.left, t.forward, t.left, t.forward,
        t.forward, t.left, t.forward]
list_turtle = [one, four, one, seven_number, zero, zero]

for i in list_turtle:
    counter = 0
    if i == one:
        turtle_one()
    for k in i:
        if i == four and k == four[1] or i == seven_number and k == seven_number[0] :
            k(x_constanta / 2)
        if i == seven_number and k == seven_number[5] and counter == 5 or\
                i == zero and k == zero[0] and counter == 0:
            k(-60)
        if i == zero and k == zero[3] and counter == 3 or i == zero and k == zero[8]:
            k(30)
        k(x_constanta)
        counter += 1
    transition()




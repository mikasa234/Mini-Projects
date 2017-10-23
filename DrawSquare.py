import turtle
def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    count = 0
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for count in range(0,36):
        c = 0
        while c<4:
            brad.forward(100)
            brad.right(90)
            c=c+1
        brad.right(10)
        

    window.exitonclick()
draw_square()

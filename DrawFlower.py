import turtle

def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")
    count = 0
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(6)

    circle = 0
    while circle < 36:
        brad.circle(30)
        brad.right(10)
        circle = circle+1

    triangle = 0
    while triangle < 36:
        t = 0
        while t < 6:
            brad.forward(50)
            brad.right(60)
            t = t+1
        brad.right(10)
        triangle = triangle + 1
        
    for count in range(0, 36):
        c = 0
        while c<2:
            brad.forward(150)
            brad.right(120)
            brad.forward(150)
            brad.right(60)
            c=c+1
        brad.right(10)
    window.exitonclick()
draw_flower()

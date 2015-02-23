import turtle

def draw_turtle():
    window = turtle.Screen()
    window.bgcolor('black')

    alice = turtle.Turtle()
    alice.color('green')
    alice.shape('turtle')

    for i in range(36):
        alice.forward(100)
        alice.left(30)
        alice.forward(100)
        alice.color('white')
        alice.circle(20)
        alice.color('green')
        alice.left(150)
        alice.forward(100)
        alice.left(30)
        alice.forward(100)
        alice.left(160)

    alice.right(90)
    alice.forward(300)
        
    window.exitonclick()

draw_turtle()

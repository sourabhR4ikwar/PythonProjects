import turtle
bob = turtle.Turtle()
print(bob)
bob.pd()
def square(x):
    for i in range(4):
        x.fd(100)
        x.rt(90)

square(bob);
bob.mainloop()

#Challenge1.py

import turtle as trtl

painter = trtl.Turtle()

#say Hello
painter.color("red")
painter.print("Hello!")

#ask how old they are and predict
painter.color("green")
a=input("How old are you?")
while(a<2):
    a=a*365
    print("You have ben alive for","a","years")

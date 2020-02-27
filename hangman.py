from __future__ import print_function 
import turtle
import time
wn = turtle.Screen()
hamza = turtle.Turtle()
hamza.backward(100)
hamza.forward(50)
hamza.right(-90)
hamza.forward(300)
hamza.right(90)
hamza.forward(150)
hamza.right(90)
hamza.forward(50)
hamza.right(90)

hamza.circle(50)
hamza.penup()
hamza.setposition(100, 150)

hamza.pendown()
hamza.right(270)
hamza.forward(100)
hamza.right(45)
hamza.forward(50)
hamza.backward(50)
hamza.left(90)
hamza.forward(50)
hamza.backward(50)
hamza.right(45)
hamza.backward(75)
hamza.right(90)
hamza.forward(50)
hamza.backward(100)


lives = 6
word = 'hello'
letter = 'l'
updatedSpaces = ['_','_','_','_','_']
2
def check():
    global updatedSpaces
    global lives
    if letter in word:
        index = -1
        for i in word:
            index += 1
            if letter == i:
                updatedSpaces[index] = letter
            else:
                continue
        print (' '.join(updatedSpaces))
        #win()     
    else: 
        lives -= 1
        if lives == 0:
            print('You loser')
        #getLetter()
    
time.sleep(5)
hamza.clear()
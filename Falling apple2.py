#   a123_apple_1.py
import random
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape



wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file
letters = ["a","s","d","f"]
def make_turtles(letters):
  turtles = []
  for _ in letters: 
    t = trtl.Turtle()
    t.penup()
    draw_apple(t)
    t.goto(random.randint(-100, 100), random.randint(-10, 90))
    turtles.append(t)
    
drawer = trtl.Turtle()


apple = trtl.Turtle()
apple.penup()
# pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

# def draw_letters(letters, turtles):
#   drawers = []
#   for i in range(len(turtles)):
#     drawer = trtl.Turtle()
#     drawer.penup()
#     drawer.goto(trtl.xcor()-18,trtl.ycor()-35)
#     drawer.write(letters[i], font = ("Arial", 40, "bold"))
#     drawers.append(drawer)

def apple_fall():
  global apple
  erase_an_A()
  x = apple.xcor()
  y = apple.ycor()
  apple.goto(x,y-140)

def make_apple_turtles(letters):
  apple_turtles = []
  for _ in range(len(letters)):
    apple_turtle = trtl.Turtle()
    apple_turtle.penup()
    apple_turtle.goto(random.randint(-120, 120), random.randint(-10, 40))
    draw_apple(apple_turtle)
    apple_turtles.append(apple_turtle)
  return apple_turtles



def draw_letters(letters, apple_turtles):
  drawer_turtles = []
  for i in range(len(letters)):
    letter = letters[i]
    drawer =  trtl.Turtle()
    drawer.hideturtle()
    drawer.penup()
    apple_turtle = apple_turtles[i]
    drawer.goto(apple_turtle.xcor()-18, apple_turtle.ycor()-40)
    drawer.color("white")
    drawer.write(letter.upper(), font=("Arial", 40, "bold"))
    drawer_turtles.append(drawer)
  return drawer_turtles

def draw_an_A(drawer):
  drawer.hideturtle()
  drawer.goto(-13,-35)
  drawer.color("black")
  drawer.write("A", font=("Arial", 30, "bold"))

def erase_an_A():
  global drawer
  drawer.clear()
  
def letter(apple):
  pass

#-----function calls-----
apple_turtles = make_apple_turtles(letters)
drawer_turtles = draw_letters(letters, apple_turtles)



# draw_pear(pear)
# draw_apple(apple)
# draw_an_A(drawer)
# wn.onkeypress(apple_fall, "a")

wn.listen()
wn.mainloop()

#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image) # Make the screen aware of the new file



drawer = trtl.Turtle()


apple = trtl.Turtle()
apple.penup()
# pear = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()


def apple_fall():
  global apple
  erase_an_A()
  x = apple.xcor()
  y = apple.ycor()
  apple.goto(x,y-140)

def draw_an_A(drawer):
  drawer.hideturtle()
  drawer.goto(-13,-35)
  drawer.color("black")
  drawer.write("A", font=("Arial", 30, "bold"))

def erase_an_A():
  global drawer
  drawer.clear()
  
#-----function calls-----
# draw_pear(pear)
draw_apple(apple)
draw_an_A(drawer)
wn.onkeypress(apple_fall, "a")

wn.listen()
wn.mainloop()

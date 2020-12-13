from graphics import *

# Variable to store draw points of snowman and stars
snowman_stars = [
           Circle(Point(250,390), 100),
           Circle(Point(250, 275), 75),
           Circle(Point(250, 200), 50),
           Oval(Point(240, 210), Point(260, 215)),
           Circle(Point(230, 190), 5),
           Circle(Point(270, 190), 5),
           Circle(Point(250, 270), 5),
           Circle(Point(250, 295), 5),
           Circle(Point(250, 320), 5),
           Line(Point(320,260), Point(400, 220)),
           Line(Point(180,260), Point(100, 220)),
           Circle(Point(50,75), 4),
           Circle(Point(150,150), 4),
           Circle(Point(475,350), 4),
           Circle(Point(390,420), 4),
           Circle(Point(250,125), 4),
           Circle(Point(225,30), 4)
           ]
snowman_stars_colors = [
           color_rgb(240, 242, 245),
           color_rgb(240, 242, 245),
           color_rgb(240, 242, 245),
           'red',
           'blue',
           'blue',
           'black',
           'black',
           'black',
           'brown',
           'brown',
           'white',
           'yellow',
           'purple',
           'blue',
           'orange',
           'gray'

           ]



def main():
    win = GraphWin("My Shapes", 500, 500)
    win.setBackground(color_rgb(0, 0, 0))

# Question being asked in the middle of screen.
    txt = Text(Point(250,175), "Do you want to see a snowman floating in space? (yes / no)")
    txt.setTextColor(color_rgb(0,255,200))
    txt.setSize(12)
    txt.setFace('courier')
    txt.draw(win)

# Input box to enter answer.
    input_box = Entry(Point(250,250),10)
    input_box.draw(win)

# Do something with response from user.
    win.getMouse()
    s=(input_box.getText())

    if s.lower()== "yes":
        input_box.undraw()
        txt.undraw()
        txt = Text(Point(165,135), "Snowman drifting in space...towards the sun.")
        txt.setTextColor(color_rgb(0,255,200))
        txt.setSize(12)
        txt.setFace('courier')
        txt.draw(win)
# Animation happens if user input was "yes"
        for i in range(0,17):
            obj = snowman_stars[i]
            obj.setFill(snowman_stars_colors[i])
            obj.draw(win)
# sun size
        sunSize = 50
# points for droplets
        pnt1 = 200
        pnt2 = 275
        pnt3 = 200
        pnt4 = 275
        pnt5 = 200
        pnt6 = 275
        pnt7 = 200
        pnt8 = 325

# While loop goes on until counter is smaller than 0, and for each loop it draws the objects below.
        counter = 30
        while counter > 0:
# Water drops melting off Snowman
            droplet1 = Circle(Point(pnt1 + 25, pnt2 + 100), 5)
            droplet1.setFill(color_rgb(66, 227, 245))
            droplet2 = Circle(Point(pnt1, pnt2), 5)
            droplet2.setFill(color_rgb(66, 227, 245))

            droplet3 = Circle(Point(pnt3 + 25, pnt4 + 100), 5)
            droplet3.setFill(color_rgb(66, 227, 245))
            droplet4 = Circle(Point(pnt3, pnt4), 5)
            droplet4.setFill(color_rgb(66, 227, 245))

            droplet5 = Circle(Point(pnt5 + 25, pnt6 + 100), 5)
            droplet5.setFill(color_rgb(66, 227, 245))
            droplet6 = Circle(Point(pnt5, pnt6), 5)
            droplet6.setFill(color_rgb(66, 227, 245))

            droplet7 = Circle(Point(pnt7, pnt8), 5)
            droplet7.setFill(color_rgb(66, 227, 245))



# Sun
            sun = Circle(Point(460, 60), sunSize)
            sun.setFill("yellow")

# Drawing objects to the window.
            droplet1.draw(win)
            droplet2.draw(win)
            sun.draw(win)
# If statement to draw droplets 3 and 4 if counter is less than 20.
            if counter < 20:
                droplet3.draw(win)
                droplet4.draw(win)
# If statement to draw droplets 5 and 6 if counter is less than 10.
            if counter < 10:
                droplet5.draw(win)
                droplet6.draw(win)
# If statement to draw the middle droplet when counter reach 14.
            if counter < 15:
                droplet7.draw(win)

# Our time delay between draw() and undraw()
            time.sleep(0.2)

            sun.undraw()
            droplet1.undraw()
            droplet2.undraw()
# If statement to undraw droplets 3 and 4 if counter is less than 20.
            if counter < 20:
                droplet3.undraw()
                droplet4.undraw()
                pnt3 -= 10
                pnt4 += 10
# If statement to undraw droplets 5 and again. We change the Point() value with each loop. So it draw at a
# different spot in the next loop.
            if counter < 10:
                droplet5.undraw()
                droplet6.undraw()
                pnt5 -= 10
                pnt6 += 10
            if counter < 15:
                droplet7.undraw()
                pnt7 -= 10
                pnt8 += 10

            pnt1 -= 10
            pnt2 += 10

            sunSize += 3


# We subtract from the counter each time a loop happens, so we could eventually reach the end of the loop When
# counter is less than zero.

            counter -= 1

        sun = Circle(Point(460, 60), sunSize)
        sun.setFill("yellow")
        sun.draw(win)

# If user input is "no", then display following message and no animation.
    elif s.lower()=="no":
        input_box.undraw()
        txt.setText("I guess you will never know!")
        txt = Text(Point(259,250), 12)
        txt.setTextColor(color_rgb(0,255,200))
# If user input is something other than "yes" or "no", we through an error message.
    else:
        input_box.undraw()
        txt.setText("Error: That is not a valid response.")
        txt = Text(Point(259,250), 12)



    win.getMouse()
    win.close()
main()

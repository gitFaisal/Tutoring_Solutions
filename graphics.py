from graphics import *
import time

def main():
    win = GraphWin("Snowman drifting in space", 500, 500)
    win.setBackground(color_rgb( 0, 0, 0))
# legs
    cir = Circle(Point(250,390), 100)
    cir.setFill(color_rgb(240, 242, 245))
    cir.draw(win)
# body
    cir2 = Circle(Point(250, 275), 75)
    cir2.setFill(color_rgb(240, 242, 245))
    cir2.draw(win)
# head
    cir3 = Circle(Point(250, 200), 50)
    cir3.setFill(color_rgb(240, 242, 245))
    cir3.draw(win)
# mouth
    mouth = Oval(Point(240, 210), Point(260, 215))
    mouth.setFill('red')
    mouth.draw(win)
# eye1
    eye1 = Circle(Point(230, 190), 5)
    eye1.setFill('blue')
    eye1.draw(win)
# eye2
    eye1 = Circle(Point(270, 190), 5)
    eye1.setFill('blue')
    eye1.draw(win)
# buttons1
    btn1 = Circle(Point(250, 270), 5)
    btn1.setFill('black')
    btn1.draw(win)
# button2
    btn2 = Circle(Point(250, 295), 5)
    btn2.setFill('black')
    btn2.draw(win)
# button3
    btn3 = Circle(Point(250, 320), 5)
    btn3.setFill('black')
    btn3.draw(win)
# left arm
    arm1 = Line(Point(320,260), Point(400, 220))
    arm1.setFill("brown")
    arm1.draw(win)

# right arm
    arm2 = Line(Point(180,260), Point(100, 220))
    arm2.setFill("brown")
    arm2.draw(win)

# star 1
    star1 = Circle(Point(50,75), 4)
    star1.setFill("white")
    star1.draw(win)
# star 2
    star2 = Circle(Point(150,150), 4)
    star2.setFill("yellow")
    star2.draw(win)
# star 3
    star3 = Circle(Point(475,350), 4)
    star3.setFill("purple")
    star3.draw(win)
# star 4
    star4 = Circle(Point(390,420), 4)
    star4.setFill("blue")
    star4.draw(win)
# star 5
    star5 = Circle(Point(250,125), 4)
    star5.setFill("orange")
    star5.draw(win)
# star 6
    star6 = Circle(Point(225,30), 4)
    star6.setFill("gray")
    star6.draw(win)

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

    win.getMouse()
    win.close()





main()

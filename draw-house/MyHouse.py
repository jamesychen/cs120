import turtle

#House
def retengle(r,length,width):
    for i in range(2):
        r.forward(length)
        r.left(90)
        r.forward(width)
        r.left(90)
def move(m,x,y):
    m.penup()
    m.setposition(x,y)
    m.pendown()
    
def window(w,length,width,x,y):
    james.fillcolor("gray")
    james.begin_fill()
    w.setheading(0)
    move(james,x,y)
    retengle(james,length,width)
    james.end_fill()
    move(james,x,y+width/2)
    w.forward(length)
    w.setheading(90)
    move(james,x+length/2,y)
    w.forward(width)
def door(d,length,width,x,y):
    d.setheading(90)
    retengle(james,length,width)
    move(james,x,y)
    d.circle(4)

def bird(size,x,y):
    move(james,x,y)
    james.setheading(60)
    for i in range(2):
        for i in range (0,18):
            james.forward(size)
            james.right(9)
        james.right(180)  
        james.right(45)

def grass(g,x,y):
    move(james,x,y)
    g.setheading(90)
    g.forward(30)
    g.setposition(x,y)
    g.setheading(135)
    g.forward(20)
    g.setposition(x,y)
    g.setheading(45)
    g.forward(20)


##Window setup
mywindow = turtle.Screen()
mywindow.bgcolor("white")
mywindow.title("My House")
mywindow.setup(920,650)

#Draw time

#make a turtle
james = turtle.Turtle()
james.speed(6)
#pick a color
james.pensize(3)
james.color("black")

#horizontal line
move(james,-480,-200)
james.forward(950)
#shape for house
move(james,-180,25)
james.setheading(270)
james.fillcolor("burlywood")
james.begin_fill()
james.forward(225)
james.left(90)
james.forward(370)
james.left(90)
james.forward(225)
james.setheading(135)
james.forward(260)
james.setheading(225)
james.forward(260)
james.end_fill()
move(james,-180,25)
##roof for the house
move(james,-195,8)
james.fillcolor("brown4")
james.begin_fill()
james.setheading(45)
james.forward(284)
james.setheading(315)
james.forward(284)
james.left(90)
james.forward(28)
james.left(90)
james.forward(310)
james.left(90)
james.forward(310)
james.left(86)
james.forward(26.5)
james.end_fill()

#window
window(james,75,60,-140,-70)
window(james,75,60,65,-70)
window(james,75,60,-38,45)
#door
move(james,40,-200)
james.fillcolor("burlywood4")
james.begin_fill()
door(james,120,70,30,-150)
james.end_fill()
#chimney
move(james,142,108)
james.fillcolor("brown3")
james.begin_fill()
james.forward(81)
james.left(90)
james.forward(40)
james.left(90)
james.forward(47.5)
james.end_fill()
#sun
move(james,-305,200)
james.fillcolor("orange")
james.begin_fill()
james.circle(50)
james.end_fill()
james.setheading(180)
james.forward(40)
move(james,-205,200)
james.setheading(0)
james.forward(40)
move(james,-255,250)
james.setheading(90)
james.forward(40)
move(james,-255,150)
james.setheading(270)
james.forward(40)

#birds
bird(2,260,200)
bird(2,340,200)
bird(2,300,240)
bird(2,300,160)
#grass
james.color("green")
grass(james,-400,-200)
##grass(james,-320,-200)
grass(james,-240,-200)
grass(james,240,-200)
grass(james,320,-200)
grass(james,400,-200)

james.color("black")
#retengle
james.setheading(90)
move(james,-310,-200)
james.fillcolor("darkorange4")
james.begin_fill()
retengle(james,54,24)
james.end_fill()

#ellipse
james.setheading(90)
move(james,-320,-75)
james.color("chartreuse4")
james.shape("circle")
james.shapesize(8,10,4)

#end
turtle.done()


from turtle import Turtle, Screen

# what it has -> Attribute //object.atrribute ex.>my_screen.canvheight
# what it can do -> Method //object.method()  ex.>tom.fd(50)

tom=Turtle() #object=class
print(tom)
tom.shape("turtle")
tom.color("red", "green")
tom.fd(50)   #forward/fd     # tom.distance() ->object method
tom.right(45)
tom.bk(75)   #backward/bk
tom.circle(1)
tom.fd(100)
tom.lt(90)   #left/lt

my_screen= Screen()
print(my_screen.canvheight)  #(object.attribute)

#object methods 
my_screen.exitonclick()
  
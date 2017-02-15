import time
import turtle

#time.time = seconds since epoch
#time.mktime = converts a date/time ... to seconds since epoch


turtle.hideturtle()


def now():
    now = time.localtime(time.time())
    return now
#updated_now = turtle.ontimer(now,2)   #### THE PROBLEM IS HERE
writer = turtle.clone()
def show_time():
    fontsize = 80
    global writer
    writer.hideturtle()
    writer.penup()
    writer.goto(0,0)
    writer.pendown()
    writer.clear()
    writer.write((now()[3] ,":",  now()[4]),align = 'center',font=("Ultra", 80, "bold"))

    turtle.ontimer(show_time,1000)

show_time()
turtle.mainloop()



##class Clock():
##    def __init__(self,writer):
##        writer = turtle.clone()
##        self.writer = writer
##        
##    def now():
##        now = time.localtime(time.time())
##        return now
##
##    def show_time():
##        
##        self.writer.hideturtle()
##        self.writer.penup()
##        self.writer.goto(0,0)
##        self.writer.pendown()
##        self.writer.clear()
##        self.writer.write((now()[3] ,":",  now()[4]),align = 'center',font=("Ultra", 80, "bold"))
##
##        turtle.ontimer(show_time,1000)
##
##    show_time()
##    turtle.mainloop()
##
##
##Clock()
##
##
##

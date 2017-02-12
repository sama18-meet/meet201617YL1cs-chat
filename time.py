import time
import turtle

#time.time = seconds since epoch
#time.mktime = converts a date/time ... to seconds since epoch


turtle.hideturtle()


def now():
    now = time.localtime(time.time())
    return now
updated_now = turtle.ontimer(now,2)
##
##def show_time():
##    writer = turtle.clone()
##    writer.hideturtle()
##    writer.penup()
##    writer.goto(80,270)
##    writer.pendown()
##    writer.write((updated_now[3], ':' , updated_now[4]),align = 'center',font=("Ultra", 10, "bold"))
##
##
##turtle.ontimer(show_time,2)
##
##
##

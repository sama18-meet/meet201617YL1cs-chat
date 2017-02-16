##QUESTIONS FOR TED
##WHY CAN'T I IMPORT PICTURES?
##HOW CAN I FIX THE TIME?

### FOR LATER
### FIX THE SEND BUTTON SO THAT ITS BIG
### MAKE THE WRITER NOT WRITE OUT OF THE BOX


import time
import turtle
turtle.hideturtle()
from turtle_chat_client import Client
from turtle_chat_widgets import TextInput , Button


class TextBox(TextInput):
    def __init__(self):
        super(TextBox,self).__init__(pos=(0,-170),height=50)
    def draw_box(self):


        bigbox= turtle.clone()
        bigbox.penup()
        bigbox.goto(110,-250)
        bigbox.pendown()
        bigbox.color("black", "red")
        bigbox.begin_fill()
        bigbox.goto(110,200)
        bigbox.goto(-110,200)
        bigbox.goto(-110,-250)
        bigbox.goto(110,-250)
        bigbox.end_fill()
        bigbox.penup()

        
        box = turtle.clone()
        
        #box.hideturtle()
        box.penup()
        box.goto(self.pos[0]-self.width/2,self.pos[1]-self.height/2)
        box.pendown()
        box.goto(self.pos[0]-self.width/2,self.pos[1]+self.height/2)
        box.goto(self.pos[0]+self.width/2,self.pos[1]+self.height/2)
        box.goto(self.pos[0]+self.width/2,self.pos[1]-self.height/2)
        box.goto(self.pos[0]-self.width/2,self.pos[1]-self.height/2)
        box.penup()




    def write_msg(self):
        
        self.writer.pendown()
        self.writer.clear()
        self.writer.write(self.new_msg)
##        if len(self.new_msg) > 30:
##            self.writer.write(self.new_msg, '\r')
##            
##        
        

#
#2. All TextInput objects have an internal turtle called writer (i.e. self will
#   have something called writer).  You can write new text with it using code like
#
#   self.writer.write(a_string_variable)
#
#   and you can erase that text using
#
#   self.writer.clear()
#
#3. If you want to make a newline character (i.e. go to the next line), just add
#   \r to your string.  Test it out at the Python shell for practice
#####################################################################################
#####################################################################################

#####################################################################################
#                                  SendButton                                       #
#####################################################################################
#Make a class called SendButton, which will be a subclass of Button.
class SendButton(Button):
    def __init__(self,my_view):
        super(SendButton,self).__init__(pos=(0,-220))
        self.my_view = my_view
        sbword = turtle.clone()
        self.sbword = sbword
        sbword.pen(pencolor="yellow")
        sbword.penup()
        sbword.goto(0,-232)
        sbword.pendown()
        sbword.write("SEND", align= "center", font=("Ultra", 16, "bold"))

    def fun(self,x=None,y=None):

        
        self.my_view.send_msg()
      
 ##################################################################
#                             View                               #
##################################################################
#Make a new class called View.  It does not need to have a parent
#class mentioned explicitly.
#
#Read the comments below for hints and directions.
##################################################################
##################################################################
class View:
    _MSG_LOG_LENGTH=5 #Number of messages to retain in view
    _SCREEN_WIDTH=300
    _SCREEN_HEIGHT=600
    _LINE_SPACING=round(_SCREEN_HEIGHT/2/(_MSG_LOG_LENGTH+1))

    def __init__(self,username='Me',partner_name='Juna',partner_pic="Juna.jpg"):
        
        ###
        #Store the username and partner_name into the instance.
        ###
        self.username = username
        self.partner_name = partner_name
        self.partner_pic = partner_pic
        ###
        #Make a new client object and store it in this instance of View
        #(i.e. self).  The name of the instance should be my_client
        ###
        my_client = Client()
        self.my_client = my_client
        ###
        #Set screen dimensions using turtle.setup
        #You can get help on this function, as with other turtle functions,
        #by typing
        #
        #   import turtle
        #   help(turtle.setup)
        #
        #at the Python shell.
        ###
        turtle.setup(width=View._SCREEN_WIDTH,height=View._SCREEN_HEIGHT) # View.
        ###
        #This list will store all of the messages.
        #You can add strings to the front of the list using
        #   self.msg_queue.insert(0,a_msg_string)
        #or at the end of the list using
        #   self.msg_queue.append(a_msg_string)
        self.msg_queue=[]
        ###

        ###
        #Create one turtle object for each message to display.
        #You can use the clear() and write() methods to erase      ???????????????????????/
        #and write messages for each
        ###
        
    #Maybe I should define msg_queue_displayed
     #   for i in range(2):
##            self.msg_queue_displayed = [self.msg_queue[-1], self.msg_queue[2]]
        mqd0 = turtle.clone()
        mqd1 = turtle.clone()
        mqd2 = turtle.clone()
        mqd3 = turtle.clone()


        mqd = (mqd0,mqd1,mqd2,mqd3)
        
        self.mqd0 = mqd0
        self.mqd1 = mqd1
        self.mqd2 = mqd2
        self.mqd3 = mqd3
        self.mqd0.penup()
        self.mqd1.penup()
        self.mqd2.penup()
        self.mqd3.penup()
        self.mqd0.goto(-100,-70)
        self.mqd1.goto(-100,0)
        self.mqd2.goto(-100,70)
        self.mqd3.goto(-100,140)
        self.mqd0.pendown()
        self.mqd1.pendown()
        self.mqd2.pendown()
        self.mqd3.pendown()
        
            
            

        #Create a TextBox instance and a SendButton instance and
        #Store them inside of this instance
        ###
        self.textbox = TextBox()
        self.sendbutton = SendButton(self)
        ###
        #Call your setup_listeners() function, if you have one,
        #and any other remaining setup functions you have invented.
        ###
        turtle.listen()

        #turtle.Screen().bgcolor('orange')
        turtle.Screen().bgpic("meet2.gif")

        partner = turtle.clone()
        partner.penup()
        partner.goto(-50,220)
        partner.pendown()
        partner.write(self.partner_name, align= "left", font=("Ultra", 20, "bold"))
        

        pic = turtle.clone()
        pic.penup()
        pic.goto(-90,210)
        pic.color("black", "red")
        pic.begin_fill()
        pic.circle(30)
        pic.end_fill()

        
    def send_msg(self):
        self.my_client.send(self.textbox.new_msg)
        self.msg_queue.append(self.textbox.new_msg)
        self.textbox.clear_msg()
        self.display_msg()
        '''
        You should implement this method.  It should
        1. call the send() method of the Client object stored in this View
        instance.
        2. It should also update the list of messages,
        self.msg_queue, to include this message.
        3. It should
        clear the textbox text display (hint: use the clear_msg method).
        4. It should call self.display_msg() to cause the message
        display to be updated.
        '''

    def get_msg(self):
        return self.textbox.get_msg()

    

    def setup_listeners(self):
        '''
        Set up send button - additional listener, in addition to click,
        so that return button will send a message.
        To do this, you will use the turtle.onkeypress function.
        The function that it will take is
        self.send_btn.fun
        where send_btn is the name of your button instance

        Then, it can call turtle.listen()
        '''
        # I CANT UNDERSTAND WHAT THIS METHOOD IS SUPPOSED TO DO AND SIVAN SAID IT WORKS WITHOUT IT SO...
        pass

    def msg_received(self,msg):
        '''
        This method is called when a new message is received.
        It should update the log (queue) of messages, and cause
        the view of the messages to be updated in the display.

        :param msg: a string containing the message received
                    - this should be displayed on the screen
        '''

        
        print(msg) #Debug - print message
        show_this_msg=self.partner_name+' says:\r'+ msg
        #Add the message to the queue either using insert (to put at the beginning)
        #or append (to put at the end).
        self.msg_queue.append(show_this_msg)
        #Then, call the display_msg method to update the display
        self.display_msg()

        
    def display_msg(self):
        '''
        This method should update the messages displayed in the screen.
        You can get the messages you want from self.msg_queue
        '''

        
        if len(self.msg_queue) == 0:
            pass

        if len(self.msg_queue) == 1:
            
            self.mqd0.clear()
            self.mqd0.write(self.msg_queue[-1])

        if len(self.msg_queue) == 2:
            
            self.mqd0.clear()
            self.mqd1.clear()
            self.mqd0.write(self.msg_queue[-1])
            self.mqd1.write(self.msg_queue[-2])

        if len(self.msg_queue) == 3:

            self.mqd0.clear()
            self.mqd1.clear()
            self.mqd2.clear()
            self.mqd0.write(self.msg_queue[-1])
            self.mqd1.write(self.msg_queue[-2])
            self.mqd2.write(self.msg_queue[-3])
            
            
        if len(self.msg_queue) >= 4:
            
            self.mqd0.clear()
            self.mqd1.clear()
            self.mqd2.clear()
            self.mqd3.clear()
            self.mqd0.write(self.msg_queue[-1])
            self.mqd1.write(self.msg_queue[-2])
            self.mqd2.write(self.msg_queue[-3])
            self.mqd3.write(self.msg_queue[-4])

        

        

    def get_client(self):
        return self.my_client
##############################################################
##############################################################


#########################################################
#Leave the code below for now - you can play around with#
#it once you have a working view, trying to run you chat#
#view in different ways.                                #
#########################################################
if __name__ == '__main__':
    my_view=View()
    _WAIT_TIME=200 #Time between check for new message, ms
    def check() :
        #msg_in=my_view.my_client.receive()
        msg_in=my_view.get_client().receive()
        if not(msg_in is None):
            if msg_in==Client._END_MSG:
                print('End message received')
                sys.exit()
            else:
                my_view.msg_received(msg_in)
        turtle.ontimer(check,_WAIT_TIME) #Check recursively
    check()
    turtle.mainloop()



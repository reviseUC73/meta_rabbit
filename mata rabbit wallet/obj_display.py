from turtle import Screen, Turtle


class Obj:
    """pattern form to draw picture and text"""
    def __init__(self):
        """determine attributes of this class"""
        self.painter = Turtle()
        self.pencil = Turtle()
        self.screen = Screen()
        self.painter.hideturtle()
        self.pencil.hideturtle()

    def screen_text_pos(self, x, y, text, colors, size):
        """
        draw or write text  on your screen by determines
        a position do you will draw  color  , size text, text
        :param x: int,float
        :param y: int,float
        :param text: str
        :param colors: str
        :param size: int,float
        """
        self.painter.speed(0)
        self.painter.penup()
        self.painter.goto(x, y)
        self.painter.pendown()
        self.painter.color(colors)
        self.painter.write(text, align='center', font=("Karla", size, "bold"))
        self.painter.hideturtle()

    def draw_big_dot(self, x, y, r):
        """
        draw dot picture so that determine position and radius of dot
        :param x:
        :param y:
        :param r:
        :return:
        """
        self.painter.penup()
        self.painter.setheading(0)
        self.painter.pendown()
        self.painter.goto(x, y)
        self.painter.dot(r)

    def screen_text_pos_1(self, x, y, text, colors, size, font, f='normal'):
        """
        draw or write text pattern_1 on your screen by determines
        a position do you will draw or write color ,font , size text, text ,letter size
        :param x:int,float
        :param y:int,float
        :param text:str
        :param colors:str
        :param size:int,float
        :param font:str
        :param f:str
        :return:
        """
        self.painter.speed(0)
        self.painter.penup()
        self.painter.goto(x, y)
        self.painter.pendown()
        self.painter.color(colors)
        self.painter.write(text, align='center', font=(font, size, f))
        self.painter.hideturtle()

    def screen_text_pos_2(self, x, y, text, colors, size, al):
        """
        draw or write text pattern_2 on your screen by determines
        a position do you will draw or write color , size text, text ,letter size
        :param x:int,float
        :param y:int,float
        :param text:str
        :param colors:str
        :param size:int,float
        :param al : str
        :return:
        """
        self.painter.speed(0)
        self.painter.penup()
        self.painter.setheading(270)
        self.painter.goto(x, y)
        self.painter.pendown()
        self.painter.color(colors)
        self.painter.write(text, align=al, font=("Karla", size, "bold"))
        self.painter.hideturtle()

    def screen_text_pos_3(self, x, y, text, colors, size, al, font):
        """
        draw or write text pattern_3 on your screen by determines
        a position do you will draw or write color ,font , size text, text ,letter size
        :param x:int,float
        :param y:int,float
        :param text:str
        :param colors:str
        :param size:int,float
        :param font:str
        :param al:str
        :return:
        """
        self.painter.speed(0)
        self.painter.penup()
        self.painter.setheading(270)
        self.painter.goto(x, y)
        self.painter.pendown()
        self.painter.color(colors)
        self.painter.write(text, align=al, font=(font, size, "normal"))
        # self.painter.hideturtle()

    def screen_text_pos_4(self, x, y, text, colors, size, al='center', font='Impact'):
        """
        draw or write text pattern_4 on your screen by determines
        a position do you will draw or write color ,font , size text, text ,letter size
        :param x:int,float
        :param y:int,float
        :param text:str
        :param colors:str
        :param size:int,float
        :param font:str
        :param al:str
        :return:
        """
        self.pencil.speed(0)
        self.pencil.penup()
        self.pencil.setheading(270)
        self.pencil.goto(x, y)
        self.pencil.pendown()
        self.pencil.color(colors)
        self.pencil.clear()
        self.pencil.write(text, align=al, font=(font, size, "normal"))
        self.pencil.hideturtle()

    def draw_square(self, size_x, size_y):
        """
        draw square so that determines length and height
        :param size_x:
        :param size_y:
        """
        self.painter.forward(size_x)
        self.painter.right(90)
        self.painter.forward(size_y)
        self.painter.right(90)
        self.painter.forward(size_x)
        self.painter.right(90)
        self.painter.forward(size_y)
        self.painter.right(90)
        # self.painter.hideturtle()

    def create_logo(self):
        """add picture rabbit"""
        self.painter.setheading(0)
        self.painter.penup()
        self.painter.speed(0)
        self.painter.goto(0, 150)
        self.screen.addshape('meta.gif')  # read and add_screen
        self.painter.shape('meta.gif')

    def draw_interface(self):
        """
        draw picture
        """
        self.painter.showturtle()
        self.painter.setheading(0)
        self.painter.penup()
        self.painter.speed(0)
        self.painter.goto(0, -110)
        self.painter.color('#FFE4E1')
        self.painter.write('Meta Rabbit!', align='center', font=('Impact', 62, "normal"))
        self.painter.color('white')
        self.painter.write('Meta Rabbit!', align='center', font=('Impact', 60, "bold"))
        self.painter.penup()
        self.painter.goto(-153, 304.5)
        self.painter.pencolor('#FFE4B5')
        self.painter.pensize(8)
        self.painter.down()
        self.painter.setheading(0)
        self.draw_square(308, 308)

    def bottom_once_screen2(self, pos_x, pos_y):
        """
        draw bottom in your screen pattern 1
        :param pos_x: float , int
        :param pos_y: float , int
        """
        self.painter.penup()
        self.painter.speed(0)
        self.painter.pensize(3)
        self.painter.color('white')
        self.painter.goto(pos_x, pos_y)  # turtle
        text = self.painter
        text.pendown()
        self.draw_square(260, 50)

    def bottom_once_screen2_v2(self, pos_x, pos_y, length, height, color, size):
        """
        draw bottom in your screen pattern 2
        :param pos_x: float , int
        :param pos_y: float , int
        :param length: float , int
        :param height: float , int
        :param color: str
        :param size: float , int
        """
        self.painter.penup()
        self.painter.speed(0)
        self.painter.pensize(size)
        self.painter.color(color)
        self.painter.goto(pos_x, pos_y)  # turtle
        text = self.painter
        text.pendown()
        self.draw_square(length, height)

    def bottom_once_screen2_v3(self, pos_x, pos_y, length, height, color, size):
        """
        draw bottom in your screen pattern 3
        :param pos_x: float , int
        :param pos_y: float , int
        :param length: float , int
        :param height: float , int
        :param color: str
        :param size: float , int
        """
        self.painter.setheading(0)
        self.painter.penup()
        self.painter.speed(0)
        self.painter.pensize(size)
        self.painter.color(color)
        self.painter.goto(pos_x, pos_y)  # turtle
        self.painter.pendown()
        self.painter.begin_fill()
        self.draw_square(length, height)
        self.painter.end_fill()

    def bottom_once_screen2_v4(self, pos_x, pos_y, length, height, color_front, color_back, size_pen):
        """
        draw bottom in your screen pattern 4
        :param pos_x: float , int
        :param pos_y: float , int
        :param length: float , int
        :param height: float , int
        :param color_front: str
        :param color_back: str
        :param size_pen: float , int
        """
        self.bottom_once_screen2_v3(pos_x + 7.5, pos_y - 7.5, length, height, color_back, size_pen)
        self.bottom_once_screen2_v3(pos_x, pos_y, length, height, color_front, size_pen)

    def b_login(self):
        """draw login bottom"""
        self.painter.setheading(0)
        self.bottom_once_screen2_v2(-120, -125, 260, 50, '#FFE4E1', 5)
        self.screen_text_pos_3(20, -170, 'Login', 'white', 25, 'center', 'Impact')

    def b_register(self):
        """draw register bottom"""
        self.painter.setheading(0)
        self.bottom_once_screen2_v2(-120, -210, 260, 50, '#FFE4E1', 5)
        self.screen_text_pos_3(20, -255, 'Register', 'white', 25, 'center', 'Impact')

    def all_bottom_2(self):
        """draw all bottom in all screen 2"""
        print(self.painter.pos())
        self.painter.pencolor('#FFE4B5')  # show money
        self.draw_big_dot(5, 130, 254)
        self.painter.pencolor('snow')
        self.draw_big_dot(5, 132, 238)  # circle show money
        self.painter.pencolor('Misty rose')
        self.draw_big_dot(5, 132, 230)
        self.bottom_once_screen2_v2(-118, -30, 262, 53, '#FFE4E1', 7)
        self.bottom_once_screen2_v2(-118, -100, 262, 53, '#FFE4E1', 7)
        self.bottom_once_screen2_v2(-118, -170, 262, 53, '#FFE4E1', 7)

        self.painter.fillcolor('white')
        self.painter.penup()
        self.painter.goto(-120, -30)
        self.painter.pendown()
        self.painter.begin_fill()
        self.bottom_once_screen2(-120, -30)
        self.bottom_once_screen2(-120, -100)
        self.bottom_once_screen2(-120, -170)
        self.painter.end_fill()
        self.painter.setheading(0)
        self.painter.penup()

    def token_bottom(self):
        """draw bottom token"""
        self.bottom_once_screen2_v2(-118, -240, 262, 53, 'white', 6)
        self.painter.fillcolor('white')
        self.painter.penup()
        self.painter.goto(-120, -30)
        self.painter.pendown()
        self.painter.begin_fill()
        self.painter.pensize(3)
        self.bottom_once_screen2_v2(-115, -245, 255, 43, 'pink', 3)
        self.painter.end_fill()
        self.painter.setheading(0)

    def line_tap_bar(self):
        """draw bottom bar"""
        pen = self.painter
        pen.penup()
        pen.goto(-400, -320)
        pen.setheading(0)
        pen.pendown()
        pen.fillcolor('Misty rose')
        pen.begin_fill()
        self.draw_square(1000, 300)
        pen.end_fill()
        pen.penup()

    def obj_screen3(self):
        """draw all bottom in all screen 3"""
        self.painter.setheading(0)

        self.bottom_once_screen2_v3(-385, 345, 73, 31, 'gray26', 3)
        self.bottom_once_screen2_v3(-385, 345, 70, 28, '#FFE4E1', 3)
        self.screen_text_pos_1(-350, 320, 'back', 'gray26', 15,
                               'Impact')  # self.bottom_once_screen2_v4(-390, 365, 60, 40, '#FFE4E1','white', 3)
        self.bottom_once_screen2_v3(-125, 320, 252, 56, 'gray28', 6)
        self.screen_text_pos_1(5, 271, 'My Token', 'white', 28, 'Impact')

        self.bottom_once_screen2_v4(-385, 200, 200, 53, '#FFE4E1', 'darkolivegreen3', 3)
        self.bottom_once_screen2_v4(-115, 200, 200, 53, '#FFE4E1', 'white', 3)
        self.bottom_once_screen2_v4(150, 200, 200, 53, '#FFE4E1', 'brown3', 3)
        self.screen_text_pos_1(-280, 160, 'Buy Token', 'gray28', 18, 'Impact')
        self.screen_text_pos_1(-10, 160, 'Import Token', 'gray28', 18, 'Impact')
        self.screen_text_pos_1(250, 160, 'Sell Token', 'gray28', 18, 'Impact')

    def token_line(self):
        """draw bar bottom in all screen 3"""
        self.bottom_once_screen2_v3(-370, 110, 650, 40, 'gray28', 6)  # //y+50
        self.screen_text_pos_1(-290, 80, 'Token Name', 'yellow', 18, 'Impact')
        self.screen_text_pos_1(-100, 80, 'Amount', 'white', 18, 'Impact')
        self.screen_text_pos_1(50, 80, 'Token value', 'white', 18, 'Impact')
        self.screen_text_pos_1(200, 80, 'Total value', 'white', 18, 'Impact')

    def token_line_loop(self, y, name, amount, token_value, total_value):
        """
        draw button and text by it can determine text to you input and position for use to a for loop of screen_3 in the
        part of list token that you have in your wallet
        :param y: int,float
        :param name: str
        :param amount: int,float,str
        :param token_value: int,float,str
        :param total_value: int,float,str
        :return:
        """
        self.bottom_once_screen2_v3(-370, 110 + y, 650, 40, '#FFE4E1', 6)
        self.screen_text_pos_1(-290, 79 + y, name, 'gray28', 18, 'Impact', f='normal')
        self.screen_text_pos_1(-100, 79 + y, amount, 'gray28', 18, 'Impact')
        self.screen_text_pos_1(50, 79 + y, token_value, 'gray28', 18, 'Impact')
        self.screen_text_pos_1(200, 79 + y, total_value, 'gray28', 18, 'Impact')

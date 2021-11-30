from account import Account
from wallet import my_wallet
from token_ import Token
import json
# from super_ import Super_run
from turtle import Screen, Turtle, done


class Obj:
    def __init__(self):
        self.painter = Turtle()
        # self.super_run = Super_run(Screen())
        self.screen = Screen()
        # self.obj_wallet = my_wallet('', 0)
        # self.obj_account = Account('', '', '')

    def screen_text_pos(self, x, y, text, colors, size):
        self.painter.speed(0)
        self.painter.penup()
        self.painter.goto(x, y)
        self.painter.pendown()
        self.painter.color(colors)
        self.painter.write(text, align='center', font=("Karla", size, "bold"))
        self.painter.hideturtle()

    def draw_circle_(self, x, y, r):
        self.painter.penup()
        self.painter.setheading(0)
        self.painter.goto(x, y - r)
        self.painter.pendown()
        self.painter.dot(r)
        # self.painter.circle(r)
        self.painter.penup()
        self.painter.goto(x, y + r)

    def draw_big_dot(self, x, y, r):
        self.painter.penup()
        self.painter.setheading(0)
        self.painter.pendown()
        self.painter.goto(x, y)
        self.painter.dot(r)

    def screen_text_pos_2(self, x, y, text, colors, size, al):
        self.painter.speed(0)
        self.painter.penup()
        self.painter.setheading(270)
        self.painter.goto(x, y)
        self.painter.pendown()
        self.painter.color(colors)
        self.painter.write(text, align=al, font=("Karla", size, "bold"))
        self.painter.hideturtle()

    # def start_screen(self):
    #     self.screen.title('META RABBIT')
    #     self.screen.bgcolor('pink')
    #     self.screen.listen()

    def start_screen(self):
        self.screen.title('META RABBIT')
        self.screen.bgcolor('pink')
        self.screen.listen()

    # def start_screen(self):
    #     self.super_run.your_screen.title('META RABBIT')
    #     self.super_run.your_screen.bgcolor('pink')
    #     self.super_run.your_screen.listen()
    #     self.super_run.your_screen.onclick(self.super_run.super_access)
    #     obj_wallet = self.super_run.super_wallet
    #     print(obj_wallet)
    #     if not isinstance(obj_wallet, my_wallet):
    #         print('fwf')
    #         pass
    #     else:
    #         if obj_wallet.your_address == '':
    #             self.screen_text_pos(15, -95, 'Sorry, your password was incorrect. Please double-check your password.',
    #                                  'yellow')

    def draw_square(self, size_x, size_y):
        self.painter.forward(size_x)
        self.painter.right(90)
        self.painter.forward(size_y)
        self.painter.right(90)
        self.painter.forward(size_x)
        self.painter.right(90)
        self.painter.forward(size_y)
        self.painter.right(90)
        self.painter.hideturtle()

    def draw_triangle(self, size):
        self.painter.forward(size)
        self.painter.left(120)
        self.painter.forward(size)
        self.painter.left(120)
        self.painter.forward(size)
        self.painter.left(120)
        self.painter.hideturtle()

    def pen_start(self, x, y, color=None, size=None):
        self.painter.setheading(0)
        self.painter.penup()
        if color is not None:
            self.painter.pencolor(color)
        if size is not None:
            self.painter.pensize(size)
        self.painter.goto(x, y)
        self.painter.pendown()

    def create_logo(self):
        self.painter.penup()
        self.painter.speed(0)
        self.painter.goto(0, 150)
        self.screen.addshape('meta.gif')  # read and add_screen
        self.painter.shape('meta.gif')

        # show display

    def defeat_screen(self):
        self.screen.title('META RABBIT')
        self.screen.bgcolor('pink')
        self.screen.listen()

    def screen_text_1(self):
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
        self.draw_square(308, 308)
        self.painter.hideturtle()

    def b_login(self):
        self.painter.speed(0)
        self.painter.pensize(3)
        self.painter.color('#FFE4E1')
        self.painter.penup()
        self.painter.goto(-120, -125)  # turtle
        text_login = self.painter
        text_login.pendown()
        self.draw_square(260, 50)
        text_login.penup()
        text_login.goto(20, -170)
        text_login.pendown()
        text_login.color('white')
        text_login.write('Login', align='center', font=("Karla", 30, "bold"))
        text_login.hideturtle()

    def b_register(self):
        self.painter.speed(0)
        self.painter.pensize(3)
        self.painter.color('#FFE4E1')
        self.painter.penup()
        self.painter.goto(-120, -210)  # turtle
        self.painter.pendown()
        self.draw_square(260, 50)
        self.painter.penup()
        self.painter.goto(20, -260)
        self.painter.pendown()
        self.painter.color('white')
        self.painter.write('Register', align='center', font=("Karla", 30, "bold"))
        self.painter.hideturtle()

    def bottom_once_screen2(self, pos_x, pos_y):
        self.painter.penup()
        self.painter.speed(0)
        self.painter.pensize(3)
        self.painter.color('white')

        self.painter.goto(pos_x, pos_y)  # turtle
        text = self.painter
        text.pendown()
        self.draw_square(260, 50)

    def bottom_once_screen2_v2(self, pos_x, pos_y, length, height, color, size):
        self.painter.penup()
        self.painter.speed(0)
        self.painter.pensize(size)
        self.painter.color(color)
        self.painter.goto(pos_x, pos_y)  # turtle
        text = self.painter
        text.pendown()
        self.draw_square(length, height)

    def draw_screen2_line(self):
        self.painter.speed(0)
        self.painter.penup()
        self.painter.pendown()
        self.painter.goto(-385, 260)
        self.painter.pencolor('gray')
        self.painter.pensize(2)
        self.painter.forward(900)

        self.painter.penup()
        self.painter.goto(-385, 40)
        self.painter.pendown()
        self.painter.pencolor('gray')
        self.painter.pensize(2)
        self.painter.forward(900)

        self.painter.penup()
        self.painter.goto(180, 260)
        self.painter.pendown()
        self.painter.pencolor('gray')
        self.painter.pensize(2)
        self.painter.right(90)
        self.painter.forward(10000)
        self.painter.left(90)

        self.painter.penup()
        self.painter.goto(-180, 260)
        self.painter.pendown()
        self.painter.pencolor('gray')
        self.painter.pensize(2)
        self.painter.right(90)
        self.painter.forward(10000)

    def all_bottom_2(self):
        self.painter.pencolor('#FFE4B5')
        self.draw_big_dot(3, 132, 235)  # show money
        self.painter.pencolor('white')
        self.draw_big_dot(0, 132, 223.5)  # circle show money

        self.painter.pendown()

        self.pen_start(-103, 132, '#FFE4E1', 7)
        self.draw_square(300, 200)
        self.painter.pensize(10)
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

        #
        # self.painter.penup()
        # self.painter.goto(-230, 320)
        # self.painter.pendown()
        # self.painter.pencolor('gray')
        # self.painter.right(90)
        # self.painter.pensize(2)
        # self.painter.forward(10000)

    # def screen_2(self):
    #     self.super_run.your_screen.clearscreen()

    # def shown_screen2(self):

# def bottom(self,x,y):

# def bo_login(self):
#     self.

# def main_account(self):
#     self.main_account = Account()
#     print('Main menu\n'
#       '1. register\n'
#       '2. login\n')
#
# num = int(input('enter menu number >> '))
# username = input('username : ')
# password = input('password : ')
# print('')
# if num == 1:
#     user1 = Account(username, password, '')
#     user1.create_account()
# elif num == 2:
#     user_wallet = my_wallet('', 0)
#     user_wallet.login(username, password)
#
#     if user_wallet.your_address != '':
#         print(user_wallet)
#         print('')
#         print('Menu choice\n'
#               '1. Deposit\n'
#               '2. Withdraw\n'
#               '3. Transfer\n'
#               '4. Import Token\n'
#               '5. Buy Token\n'
#               '6. Sell Token\n'
#               ' Exit \n')
#
#         print('')
#
#         x = input('Choice >> ')
#         if x == '1':
#             money = float(input('Amount to deposit : '))
#             user_wallet.deposit(money)
#             print(user_wallet)
#
#         elif x == '2':
#             money = float(input('Amount to withdraw : '))
#             user_wallet.withdraw(money)
#             print(user_wallet)
#
#         elif x == '3':
#             to_address = input('Enter address to transfer >>> ')
#             money = float(input('Balance money : '))
#             user_wallet.balance_transfer(to_address, money)
#         elif x == '4':
#             address = input('input_contract >>> ')
#             user_wallet.import_token(address)
#             print('')
#             print(user_wallet)
#             pass
#         elif x == '5':
#             name_token = input('Name token: ')
#             price = float(input('Price : '))
#             user_wallet.buy_token(name_token, price)
#             print('')
#             print(user_wallet)
#         elif x == '6':
#             name_token = input('Name token: ')
#             amount = float(input('Amount : '))
#             user_wallet.sell_token(name_token, amount)
#             print('')
#             print(user_wallet)
#
#
# else:
#     print('your username or password is wrong please check it again')

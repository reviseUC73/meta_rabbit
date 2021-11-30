from account import Account
from wallet import my_wallet
from token_ import Token
import json
from turtle import Screen, Turtle, done
from obj_display import Obj


def click(x, y):
    print(x, y)


class Super_run:
    def __init__(self, your_screen):
        self.username = ''
        self.password = ''
        self.your_screen = your_screen
        self.super_wallet = ''
        self.super_account = ''
        self.obj = Obj()
        self.obj.painter.hideturtle()

    def super_access(self, x, y):
        self.obj.painter.clear()
        if -120 <= x <= 140 and -250 <= y <= -200:
            self.username = self.your_screen.textinput("Register", 'Username : ')
            self.password = self.your_screen.textinput("Register", 'Password : ')
            user1 = Account(self.username, self.password, '')
            pen = self.obj

            if user1.create_account() == 'complete':
                text = 'Your account has been created successful'
                pen.screen_text_pos(15, -300, text, '#32CD32', 13)

            elif user1.create_account() == 'nope_have':
                text = 'This username has been used'
                pen.screen_text_pos(15, -300, text, '#FF8C00', 12)

            elif user1.create_account() == 'nope_less':
                text = 'Your password have to include number more than one and there \n         ' \
                       'must be more t han 6 numbers ' \
                       'and letters combined'
                pen.screen_text_pos(15, -300, text, '#FFA500', 11)

        elif -120 <= x <= 140 and -165 <= y <= -115:
            self.username = self.your_screen.textinput("Login", 'Username :')
            self.password = self.your_screen.textinput("Login", 'Password : ')
            self.super_wallet = my_wallet('', 0)
            self.super_wallet.login(self.username, self.password)
            x = self.super_wallet.your_address
            access_wallet = self.super_wallet
            print(access_wallet)
            if access_wallet.your_address == '':
                pen = self.obj
                text = 'Sorry, your password was incorrect. Please double-check your password.'
                pen.screen_text_pos(15, -295, text, 'red', 10)
            else:
                self.new_screen_2()
                self.show_address()

    def screen_new(self):
        self.your_screen.title('META RABBIT')
        self.your_screen.bgcolor('pink')
        self.your_screen.listen()
        # self.obj.draw_circle(200,200, 50)
        # self.obj.painter.goto(200, 200)
        # self.obj.painter.dot(3)
        # self.buttons_screen2(-330,226)
        self.your_screen.onclick(self.super_access)

        # self.your_screen.onclick(click)

    def show_address(self):
        pen = self.obj
        text = self.super_wallet.your_address
        pen.screen_text_pos_2(-15, 285, text, '#FFFAFA', 10, 'left')
        self.obj.painter.penup()
        self.obj.painter.goto(350, 295)
        self.obj.painter.color('gray')
        self.obj.painter.pendown()
        self.obj.painter.goto(350, 305)
        self.obj.draw_square(22, 380)
        self.obj.draw_square(24, 382)
        self.obj.painter.goto(345, 295)
        self.obj.painter.color('gray')
        self.obj.painter.dot(28)
        self.obj.painter.color('#3CB371')
        self.obj.painter.dot(22)
        self.obj.painter.color('#00FA9A')
        self.obj.painter.dot(15)
        self.obj.painter.penup()

    def new_screen_2(self):
        self.your_screen.clearscreen()
        self.your_screen.bgcolor('pink')
        self.your_screen.listen()
        self.obj.painter.pensize(2)
        self.obj.painter.pendown()
        self.obj.painter.speed(0)
        self.obj.all_bottom_2()

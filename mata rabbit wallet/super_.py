from account import Account
from wallet import my_wallet
from obj_display import Obj
from turtle import Turtle


class Super_run:
    """Bring the classes together and show them to the display page."""

    def __init__(self, your_screen):
        """determine attributes in this class"""
        self.username = ''
        self.password = ''
        self.your_screen = your_screen
        self.super_wallet = ''
        self.super_account = ''
        self.obj = Obj()
        self.obj_2 = Obj()
        self.obj_3 = Obj()
        self.pencil_ = Turtle()
        self.obj_3.painter.hideturtle()
        self.obj.painter.hideturtle()
        self.obj_2.painter.hideturtle()
        self.pencil_.hideturtle()
        self.party_dict = {'name': '', 'money': 0}

    # These are method using for print the value of x and y to make the buttons
    def super_access(self, x, y):
        """
        It's a method used to specify a point in your screen that if you click that point your code will behave
        differently. by using together with onscreenclick() This will execute the login and register command,
        which is a method of class my_wallet.

        :param x: int,string
        :param y: int,string
        """
        self.obj.painter.clear()
        # position of register bottom and condition of them
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
                       'must be more than 8 numbers or equal' \
                       'and letters combined'
                pen.screen_text_pos(15, -330, text, '#FFA500', 11)
        # position of login bottom and condition
        elif -120 <= x <= 140 and -165 <= y <= -115:
            self.username = self.your_screen.textinput("Login", 'Username :')
            self.password = self.your_screen.textinput("Login", 'Password : ')
            self.super_wallet = my_wallet('', 0)
            self.super_wallet.login(self.username, self.password)
            if self.super_wallet.your_address == '':
                pen = self.obj
                text = 'Sorry, your password was incorrect. Please double-check your password.'
                pen.screen_text_pos(15, -295, text, 'red', 10)
            else:
                self.obj_3.painter.clear()
                self.your_screen.clearscreen()
                self.new_screen_2()  # login complete
                self.show_address_2()
                self.your_screen.onclick(self.chose_point)

    def screen_new(self):
        """show interface of your screen 1 (login/register page)"""
        self.your_screen.setup(800, 750)
        self.your_screen.title('META RABBIT')
        self.your_screen.bgcolor('pink')
        self.your_screen.listen()
        self.obj.painter.pendown()
        self.obj_2.painter.setheading(0)
        self.obj_2.draw_interface()
        self.obj_2.b_login()
        self.obj_2.b_register()
        self.your_screen.onclick(self.super_access)
        self.obj_2.create_logo()

    def show_address_2(self):
        """show address of your wallet in screen"""
        pen = self.obj
        text = self.super_wallet.your_address
        pen.bottom_once_screen2_v3(-320, 354, 381, 30, '#FFE4E1', 3)
        pen.bottom_once_screen2_v3(-320, 352, 378, 23, 'white', 3)
        pen.screen_text_pos_3(-387.5, 331.5, "Address : ", 'gray26', 11, 'left', 'Impact')
        pen.screen_text_pos_2(-300, 333, text, 'pink', 10, 'left')
        pen.painter.setheading(0)
        pen.bottom_once_screen2_v3(-385, -330, 73, 31, 'gray26', 3)
        pen.bottom_once_screen2_v3(-385, -330, 70, 28, 'pink', 3)
        pen.screen_text_pos_3(-374, -354, "Log out", 'white', 13, 'left', 'Impact')

    def show_balance(self):
        """show balance of your wallet in screen"""
        pen = self.obj
        text = self.super_wallet.balance
        pen.painter.speed(0)
        pen.screen_text_pos_1(8, 170, 'Your Balance', 'white', 20, 'Impact')
        pen.screen_text_pos_1(8, 100, f'{text:.2f}', 'white', 40, 'Impact')
        pen.screen_text_pos_1(8, 52.5, 'USDT', 'white', 20, 'Impact')
        pen.screen_text_pos_1(13, 170, 'Your Balance', 'gray28', 20, 'Impact')
        pen.screen_text_pos_1(13, 100, f'{text:.2f}', 'gray28', 40, 'Impact')
        pen.screen_text_pos_1(11, 52.5, 'USDT', 'lightpink', 20, 'Impact')

    def new_screen_2(self):
        """show screen of wallet user and bottom for put to call function in screen 2 """
        self.pencil_.hideturtle()
        self.your_screen.clearscreen()
        self.your_screen.bgcolor('pink')
        self.your_screen.listen()
        self.obj.painter.pensize(2)
        self.obj.painter.pendown()
        self.obj.painter.speed(0)
        self.obj.all_bottom_2()
        self.obj.line_tap_bar()
        self.obj.token_bottom()
        self.show_balance()
        self.obj.screen_text_pos_1(10, -75, 'Deposit', 'pink', 22, 'Impact')
        self.obj.screen_text_pos_1(10, -145, 'Withdraw', 'pink', 22, 'Impact')
        self.obj.screen_text_pos_1(10, -215, 'Transfer', 'pink', 22, 'Impact')
        self.obj.screen_text_pos_1(10, -285, 'My Token', 'white', 22, 'Impact')

    def put_transfer(self, x, y):
        """
        show transfer popup by and determine function in each case position that your click
        :param x: float,int
        :param y: float,int
        """
        pen = self.obj_2
        # input address transfer and keep it in self.party_dict so that attribute of class.
        if -302 <= x <= 85 and 263 <= y <= 290:
            pen.painter.setheading(0)
            pen.bottom_once_screen2_v3(-300, 286, 383, 23, 'pink', 3)
            pen.bottom_once_screen2_v3(-300, 290, 383, 23, 'white', 3)
            to_address = self.your_screen.textinput("Transfer", 'Transfer to : ')
            pen.screen_text_pos_2(-290, 270, to_address, 'pink', 10, 'left')
            self.party_dict['name'] = to_address

        # input money that transfer and keep it in self.party_dict so that attribute of class.
        elif -302 <= x <= 85 and 195 <= y <= 220:
            pen.painter.setheading(0)
            pen.bottom_once_screen2_v3(-300, 216, 383, 23, 'pink', 3)
            pen.bottom_once_screen2_v3(-300, 220, 383, 23, 'white', 3)
            balance = self.your_screen.textinput("Transfer", 'Balance : ')
            pen.screen_text_pos_2(-290, 200, balance, 'pink', 10, 'left')
            self.party_dict['money'] = balance

        #  use balance_transfer_2 of my_wallet class of value in parameter come from self.party_dict and when it will
        # re-screen for show your present data
        elif -76 <= x <= 81 and 95 <= y <= 151:  # confirm
            if self.super_wallet.balance_transfer_2(self.party_dict['name'], float(self.party_dict['money'])) == 'yes':
                self.new_screen_2()  # login complete
                self.show_address_2()
                self.your_screen.onclick(self.chose_point)
            else:
                pen.bottom_once_screen2_v3(-300, 180, 350, 20, 'gray87', 3)
                pen.screen_text_pos_4(-280, 160, self.super_wallet.balance_transfer_2(self.party_dict['name'],
                                                                                      float(self.party_dict['money'])),
                                      'gray26', 10, 'left', 'Impact')
        # re-screen and show your present data
        elif -336 <= x <= -172 and 95 <= y <= 151:  # cancel

            self.new_screen_2()  # login complete
            self.show_address_2()
            self.your_screen.onclick(self.chose_point)

    # determine
    def chose_point(self, x, y):
        """
        when click button in screen 2 it show in each function by depend on position that your click
        :param x: integer,float
        :param y: integer,float
        """
        # deposits bottom use deposit methods of class my wallet and re-screen for show present data of my wallet
        if -120 <= x <= 150 and -88 <= y <= -30:
            money = self.your_screen.textinput("Deposits", 'Amount of money: ')
            self.super_wallet.deposit(float(money))
            self.new_screen_2()  # login complete
            self.show_address_2()
            self.your_screen.onclick(self.chose_point)

        # withdraw bottom use withdraw methods of class my wallet and re-screen for show present data of my wallet
        elif -120 <= x <= 150 and -155 <= y <= -100:  # withdraw
            money = self.your_screen.textinput("Withdraws", 'Amount of money: ')
            self.super_wallet.withdraw(float(money))
            self.new_screen_2()  # login complete
            self.show_address_2()
            self.your_screen.onclick(self.chose_point)

        # transfer bottom by use combination with onclick methods and put transfer methods
        elif -120 <= x <= 150 and -226 <= y <= -168:  # transfer
            pen = self.obj
            self.obj.painter.setheading(0)
            self.obj.bottom_once_screen2_v4(-388.5, 300, 500, 190, '#FFE4E1', 'gray87', 3)
            self.obj.bottom_once_screen2_v4(-75, 150, 150, 50, 'white', 'pink', 3)
            self.obj.bottom_once_screen2_v4(-335, 150, 150, 50, 'pink', 'white', 3)
            pen.screen_text_pos_3(-45, 110, "Confirm ", 'pink', 20, 'left', 'Impact')
            pen.screen_text_pos_3(-300, 110, "Cancel ", 'white', 20, 'left', 'Impact')
            pen.painter.setheading(0)
            pen.bottom_once_screen2_v3(-300, 286, 383, 23, 'pink', 3)
            pen.bottom_once_screen2_v3(-300, 290, 383, 23, 'white', 3)
            pen.screen_text_pos_3(-386, 270, "Transfer To : ", 'gray26', 11, 'left', 'Impact')
            pen.screen_text_pos_2(-290, 270, '..............', 'pink', 10, 'left')
            pen.painter.setheading(0)
            pen.bottom_once_screen2_v3(-300, 216, 383, 23, 'pink', 3)
            pen.bottom_once_screen2_v3(-300, 220, 383, 23, 'white', 3)
            pen.screen_text_pos_3(-386, 200, "Balance : ", 'gray26', 11, 'left', 'Impact')
            pen.screen_text_pos_2(-290, 200, '..............', 'pink', 10, 'left')
            pen.painter.setheading(0)
            self.your_screen.onclick(self.put_transfer)

        # my token bottom
        elif -120 <= x <= 150 and -295 <= y <= -239:  # my_token
            self.new_screen_3()

        # come back login and register interface (first page)
        elif -389 <= x <= -312 and -357 <= y <= -330:  # log out
            self.your_screen.clear()
            self.screen_new()
            self.obj_2.draw_interface()
            self.obj_3.create_logo()
            self.pencil_.setheading(0)
            self.pencil_.penup()
            self.pencil_.speed(0)
            self.pencil_.goto(0, 150)
            self.pencil_.showturtle()
            self.your_screen.addshape('meta.gif')
            self.pencil_.shape('meta.gif')

    def click_screen_3(self, x, y):
        """
        Use with the onclick method by it will determine position x axis and y axis by if we click the
        point that we determine it will show different function and how it works
        :param x: float,int
        :param y: float,int
        """
        self.obj_3.painter.clear()
        # Buy token by use buy_token_ methods of class my wallet and show result in your screen
        if -385.0 <= x <= -180 and 140 <= y <= 200:
            name = self.your_screen.textinput("Buy Token", 'Name_token : ')
            money = float(self.your_screen.textinput("Buy Token", 'Price : '))
            if self.super_wallet.buy_token_(name, money) == 'complete':
                self.new_screen_3()
            else:
                self.obj_3.bottom_once_screen2_v3(-360, 250, 700, 25, 'gray26', 3)
                self.obj_3.screen_text_pos_1(-5, 230, self.super_wallet.buy_token_(name, money), 'yellow', 10, 'Impact')

        # Import token by use import_token_ methods of class my wallet and show result in your screen
        elif -120 <= x <= 95 and 140 <= y <= 200:
            address = self.your_screen.textinput("Import Token", 'Contract : ')
            if self.super_wallet.import_token_(address) == 'complete':
                self.new_screen_3()
            else:
                self.obj_3.bottom_once_screen2_v3(-360, 250, 700, 25, 'gray26', 3)
                self.obj_3.screen_text_pos_1(-5, 230, self.super_wallet.import_token_(address), 'yellow', 10, 'Impact')

        # Sell token by use sell_token methods of class my wallet and show result in your screen
        elif 150 <= x <= 362 and 140 <= y <= 200:
            name_token = self.your_screen.textinput("Sell Token", 'Name_token : ')
            amount = float(self.your_screen.textinput("Sell Token", 'Amount : '))
            if self.super_wallet.sell_token(name_token, amount) == 'complete':
                self.new_screen_3()
            else:
                self.obj_3.bottom_once_screen2_v3(-360, 250, 700, 25, 'gray26', 3)
                self.obj_3.screen_text_pos_1(-5, 230, self.super_wallet.sell_token(name_token, amount), 'yellow', 10,
                                             'Impact')
        # back it will open screen_2 and close present screen
        elif -385 <= x <= -310 and 310 <= y <= 345:
            self.new_screen_2()  # login complete
            self.show_address_2()
            self.your_screen.onclick(self.chose_point)

    def new_screen_3(self):
        """
        show screen_3 of wallet on your token when you input bottom that determine position x and y axis
        by use click_screen_3 method with onclick method
        """
        self.your_screen.clearscreen()
        self.obj.painter.clear()
        self.obj_2.painter.clear()
        self.your_screen.bgcolor('pink')
        self.your_screen.listen()
        self.obj.obj_screen3()
        self.obj_2.token_line()
        self.obj_2.line_tap_bar()
        wallet = self.super_wallet.all_token
        num = 0
        for i in wallet:
            num -= 60
            self.obj.token_line_loop(num, i, f"{wallet[i]['Amount']:.3f}", f"{wallet[i]['Token value']:.3f}",
                                     f"{wallet[i]['Total value']:.3f}")
        self.your_screen.onclick(self.click_screen_3)

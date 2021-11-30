from account import Account
from wallet import my_wallet
from token_ import Token
import json
from turtle import Screen, done, Turtle, Pen
from obj_display import Obj
from super_ import Super_run





# screen_interface = Obj()
# screen_interface.start_screen()
# screen 1
# def check_pos():
#     screen_interface = Super_run(Screen())
#     screen_interface.your_screen.title('META RABBIT')
#     screen_interface.your_screen.bgcolor('pink')
#     screen_interface.your_screen.listen()
#     screen_interface.your_screen.onclick(click)


# check_pos()
# x = Obj()
# x.start_screen()
a = Super_run(Screen())
a.screen_new()

rabbit_1 = Obj()
background_1 = Obj()
rabbit_1.create_logo()
background_1.screen_text_1()

bottom_login = Obj()
bottom_login.b_login()
bottom_register = Obj()
bottom_register.b_register()

done()

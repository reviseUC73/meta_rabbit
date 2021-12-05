from account import Account
from wallet import my_wallet
from token_ import Token
import json
from turtle import Screen, done, Turtle
from obj_display import Obj
from super_ import Super_run

# # show = Screen()
# # show.title('META RABBIT')
# # show.bgcolor('pink')
# #
# # login = Turtle()
# # login.setup()
# #
# #
# # done()
#
# import turtle
# import time
# from functools import partial
#
# # screen_width = 600
# # screen_height = 500
# #
# # screen = turtle.Screen()
# # screen.setup(screen_width, screen_height)
# # screen.tracer(0)
# # screen.title('Text Input Python Turtle')
# # screen.bgcolor('#111111')
# #
# #
# # t = turtle.Pen()
# # number = int(turtle.numinput("변 또는 동그라미의 수",
# #              "변 또는 동그라미의 수를 입력해 주세요:",6))
# # shape = turtle.textinput("어떤 모양을 원하십니까?",
# #                          "p는 세모,r는 동그라미:")
# # for x in range(number):
# #     if shape == 'r':
# #         t.circle(100)
# #     else:
# #         t.forward(150)
# #     t.left(360/number)
#
# class TextBox:
#     def __init__(self, x=-150, y=75, w=300, h=50, drawing_pen: turtle.Turtle = None):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         if drawing_pen is not None:
#             self.pen = drawing_pen
#         else:
#             self.pen = turtle.Turtle()
#             self.pen.hideturtle()
#             self.pen.penup()
#             self.pen.color('white')
#         self.text = ''
#         self.text_size = int(self.h * 0.4)
#         self.blink_timer = time.time()
#         self.is_cursor_visible = True
#         self.active = False
#
#     def add_letter(self, letter: str):
#         if not self.active:
#             return
#         if len(self.text) <= self.w // self.text_size:
#             self.text += letter
#
#     def remove_letter(self):
#         if not self.active:
#             return
#         self.text = self.text[0: -1]
#
#     def change_active_state(self, x, y):
#         self.active = False
#         if self.x <= x <= self.x + self.w:
#             if self.y - self.h <= y <= self.y:
#                 self.active = True
#                 return
#
#     def update(self):
#         if time.time() - self.blink_timer > 0.5:
#             self.blink_timer = time.time()
#             self.is_cursor_visible = not self.is_cursor_visible
#
#     def draw(self):
#         self.pen.clear()
#         self.pen.penup()
#         self.pen.goto(self.x, self.y)
#         self.pen.pendown()
#         for i in range(2):
#             self.pen.forward(self.w)
#             self.pen.right(90)
#             self.pen.forward(self.h)
#             self.pen.right(90)
#         if self.active:
#             if self.is_cursor_visible:
#                 text = self.text + '_'
#             else:
#                 text = self.text + ' '
#         else:
#             if self.text == '':
#                 text = 'Click to Type'
#             else:
#                 text = self.text
#         self.pen.penup()
#         self.pen.goto(self.x + self.w // 2, self.y - self.h * 0.85)
#         self.pen.write(text, align='center', font=('consolas', self.text_size, 'normal'))
#
#
# text_box = TextBox()
# screen = Screen()
# screen.onclick(text_box.change_active_state, 1)
# # adding key bindings
# # add more characters to the string to bind them as well
# for new_letter in 'abcdefghijklmnopqrstuvwxyz':
#     func = partial(text_box.add_letter, new_letter)
#     screen.onkeypress(func, new_letter)
#     func = partial(text_box.add_letter, new_letter.upper())
#     screen.onkeypress(func, new_letter.upper())
# screen.onkeypress(lambda: text_box.add_letter(' '), 'space')
# screen.onkeypress(text_box.remove_letter, 'BackSpace')
# screen.listen()
#
# while True:
#     text_box.update()
#     text_box.draw()
#     screen.update()
#     time.sleep(0.01)

# import turtle
# import time
# from functools import partial
#
# screen_width = 600
# screen_height = 500
#
# screen = turtle.Screen()
# screen.setup(screen_width, screen_height)
# screen.tracer(0)
# screen.title('Text Input Python Turtle')
# screen.bgcolor('#111111')
#
#
# class TextBox:
#     def __init__(self, x=-150, y=75, w=300, h=50, drawing_pen: turtle.Turtle = None):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         if drawing_pen is not None:
#             self.pen = drawing_pen
#         else:
#             self.pen = turtle.Turtle()
#             self.pen.hideturtle()
#             self.pen.penup()
#             self.pen.color('white')
#         self.text = ''
#         self.text_size = int(self.h * 0.4)
#         self.blink_timer = time.time()
#         self.is_cursor_visible = True
#         self.active = False
#
#     def add_letter(self, letter: str):
#         if not self.active:
#             return
#         if len(self.text) <= self.w // self.text_size:
#             self.text += letter
#
#     def remove_letter(self):
#         if not self.active:
#             return
#         self.text = self.text[0: -1]
#
#     def change_active_state(self, x, y):
#         self.active = False
#         if self.x <= x <= self.x + self.w:
#             if self.y - self.h <= y <= self.y:
#                 self.active = True
#                 return
#
#     def update(self):
#         if time.time() - self.blink_timer > 0.5:
#             self.blink_timer = time.time()
#             self.is_cursor_visible = not self.is_cursor_visible
#
#     def draw(self):
#         self.pen.clear()
#         self.pen.penup()
#         self.pen.goto(self.x, self.y)
#         self.pen.pendown()
#         for i in range(2):
#             self.pen.forward(self.w)
#             self.pen.right(90)
#             self.pen.forward(self.h)
#             self.pen.right(90)
#         if self.active:
#             if self.is_cursor_visible:
#                 text = self.text + '_'
#             else:
#                 text = self.text + ' '
#         else:
#             if self.text == '':
#                 text = 'Click to Type'
#             else:
#                 text = self.text
#         self.pen.penup()
#         self.pen.goto(self.x + self.w // 2, self.y - self.h * 0.85)
#         self.pen.write(text, align='center', font=('consolas', self.text_size, 'normal'))
#
#
# text_box = TextBox()
#
# screen.onclick(text_box.change_active_state, 1)
# # adding key bindings
# # add more characters to the string to bind them as well
# for new_letter in 'abcdefghijklmnopqrstuvwxyz':
#     func = partial(text_box.add_letter, new_letter)
#     screen.onkeypress(func, new_letter)
#     func = partial(text_box.add_letter, new_letter.upper())
#     screen.onkeypress(func, new_letter.upper())
# screen.onkeypress(lambda: text_box.add_letter(' '), 'space')
# screen.onkeypress(text_box.remove_letter, 'BackSpace')
# screen.listen()
#
# while True:
#     text_box.update()
#     text_box.draw()
#     screen.update()
#     time.sleep(0.01)


# x1 = Screen()
#
# done()
dict_q = {
    'num1': {
        'Amount': 50.0,
        'Token value': 6.56,
        'Total value': 3664.0}
    , "num2": {
        "Amount": 1940.0,
        "Token value": 1.06,
        "Total value": 3604.0
    }
}

print(len(dict_q))
for key, val in dict_q.items():
    print(key)
    for val2 in val.values():
        print(val2)
a = Obj()
a.painter.showturtle()
a.create_logo()
done()
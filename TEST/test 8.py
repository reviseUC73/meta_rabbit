class test8:
    def __init__(self):
        self.y2 = None
        self.x = 'x'
        self.y = 'y'
        self._value = 56
        self.check(self.y)

    def check(self, y2):
        # self._z = k
        self.y2 = y2
        print(y2)

    @property
    def value(self):
        return self._value

    def g(self):
        self.z = 5

    def zzzz(self):
        self._value += 1
        print(self.value)


test = test8()
print(test.value)
test.check('y2')
test.zzzz()

#     @property
#     def z(self):
#         return self._z
# class edit_test8:
# x = test8()
# print(x.zzzz())
# print(x.z)

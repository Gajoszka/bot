class TestClass:
    __first = 22
    _two = 33
    xx_ =44

    def x(self, ff):
        return self.__first + ff


TestClass.first = "1"
print(TestClass.first)
t = TestClass()
print(t.first)
print(t.x(3))
print(t._two)
print(t.xx_)
t.first = "11"
print(TestClass.first)
print(t.first)
t.two = "2"
# print(TestClass.two)
print(t.two)



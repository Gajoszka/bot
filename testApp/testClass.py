class TestClass:

    def __init__(self) -> None:
        super().__init__()
        self.__first_ = 22
        self._two = 33
        self.xx_ = 44

    def x(self, ff):
        return self.__first_ + ff


TestClass.__first = 1
print("TestClass.__first:" + str(TestClass.__first))
# print("TestClass.__first_:" + str(TestClass.__first_))
t = TestClass()
print("t.__first: " + str(t.__first))
# print("t.__first_: " + str(t.__first_))
print("t.x(3):" + str(t.x(3)))
print("t._two:" + str(t._two))
print("t.xx_:" + str(t.xx_))
t.__first_ = 330
print("t.__first: " + str(t.__first_))
t.first = 11
print("t.first: " + str(t.first))
print("t.__first: " + str(t.__first))
print("TestClass.__first:" + str(TestClass.__first))
print("t.first: " + str(t.first))
t.two = 2
# print(TestClass.two)
print(t.two)

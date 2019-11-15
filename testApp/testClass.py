class TestClass:
    pass


TestClass.first = "1"
print(TestClass.first)
t = TestClass()
print(t.first)
t.first = "11"
print(TestClass.first)
print(t.first)
t.two = "2"
# print(TestClass.two)
print(t.two)

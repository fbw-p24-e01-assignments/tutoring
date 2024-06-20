def multiply_by_3(func):
    if type(func) == int:
        return func * 3
    return func() * 3

def plus_2(func):
    if type(func) == int:
        return func + 2
    return func() + 2

@plus_2
@multiply_by_3
def new_func():
    return 5

@multiply_by_3
@plus_2
def woohoo():
    return 2

class MyClass:
    base_value = 1

    # @property
    def time_three(self):

        return self.base_value * 9

c = MyClass()
c.base_value = 3
a = woohoo

print(new_func, woohoo)
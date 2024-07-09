# Decorators

A decorator is a function that takes another function as an argument and does something with it.

```python {"id":"01J0TDHQSAJC7XHJG1FV3G4M7H"}
def decorator(func):
    return func()
```


It is marked with a `@` symbol and needs to be placed right before a function or class decoration. The `@` symbol lets the decorator function know which function or class to take as its argument: the one whose declaration comes after the `@` statement.

Example:

```python {"id":"01J0TDAD8SFC4621KNWZ219E4P"}
@decorator # decorator function is run and takes func as its argument
def func():
    pass

@decorator # decorator function is run and takes MyClass as its argument
class MyClass:
    pass
```

### Decoration chain

You can stack multiple decorators on top of each other. They will all refer to the same function and the decorators will be run from inner to outer.

Example:

```python {"id":"01J0TE22MV3N89EWJ1GDBZR87S"}
@deco3 # runs third
@deco2 # runs second
@deco1 # runs first
def func():
    pass
```

### Special decorators

- `@property`

The `@property` decorator makes a class method into a property of the class, which means it's going to be treated as a normal attribute.

- `@staticmethod`

The `@staticmethod` decorator is used on class methods to make the `self` argument unnecessary.

### Resources

- [Primer on Python decorators](https://realpython.com/primer-on-python-decorators/#python-functions) on realpython.com
- [Decorator](https://www.programiz.com/python-programming/decorator) on programiz.com
- [Property](https://www.programiz.com/python-programming/property) on programiz.com
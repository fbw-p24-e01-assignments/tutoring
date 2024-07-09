# Monkey Patching

Monkey patching is a technique used to dynamically update the behavior of a piece of code at run-time. It is used to extend or modify the runtime code without altering the original source code.

Monkey patching is used to replace methods / classes / attributes / functions at runtime.

### How to monkey patch

1. Identify the target to monkey patch
2. Write the code that will add, modify or replace existing code
3. Apply the patch by assigning it to the target

Example:

```python {"id":"01J0TEA3KZZXZSX2Z1W6CJVXNY"}
class Robot:
    level = 0
    
    def __init__(self, name):
        self.name = name

# 1. identify the target: add speak method to Robot

# 2. write the code that will add existing code:
def add_speech(cls):
    cls.speak = lambda self, msg: print(msg)
    return cls

# 3. apply the patch by assigning it to the target:
Robot = add_speech(Robot)

```

### Resources

- [Monkey patch](https://en.wikipedia.org/wiki/Monkey_patch) on Wikipedia
- [Python monkey patching](https://www.pythontutorial.net/advanced-python/python-monkey-patching/) on pythontutorial.net
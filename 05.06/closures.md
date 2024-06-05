# Closures

### What are closures

A Python closure is a nested function that references one or more variables from its enclosing scope.

It remembers values in enclosing scopes even if they are not present in memory.

### Why use closures

- Closures can be used to avoid global values and provide data hiding, and can be an elegant solution for simple cases with one or few methods.
- A class in the Python programming language always has the `__init__` method. If you only have one extra method, an elegant solution would be to use a closure rather than a class, because this improves code readability and even reduces the programmer’s workload. Closures in Python can thus be used to avoid the needless use of a class.
- But if you need to have many functions, then go for class (OOP).

### More about closures
All function objects have a `__closure__` attribute that returns a tuple of cell objects if it is a closure function.

Example:

`print(func_var.__closure__)`

returns

`>>> (<cell at 0x0000017184915C40: str object at 0x0000017186A829B0>,)`


### Resources

- https://www.programiz.com/python-programming/closure
- https://www.geeksforgeeks.org/python-closures/
- https://www.pythontutorial.net/advanced-python/python-closures/
- https://pythontutor.com/render.html#mode=edit (from Sophia :) )

# Our Live Code

```python {"id":"01HZMNTZJX6HDG0ERWYVMNMPX7"}
def make_multiplier():
    total = 1 # 7 # 21

    def multiplier(a): # __closure__()
        nonlocal total
        total *= a
        return total

    return multiplier

time_2 = make_multiplier()

'''
In Python, a "cell object" is an internal object
used by the Python interpreter to implement closures.
'''
print(time_2.__closure__) # tuple

print(time_2(7))
print(time_2(3))
print(time_2(6))
```
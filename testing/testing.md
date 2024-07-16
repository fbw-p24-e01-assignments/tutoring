# Testing

Testing is the process of evaluating a program to identify errors by running it under different conditions.

### Unittest

Basic unittest test structure:

```python {"id":"01J06F3GCBA2NYBA478A3X70NZ"}
import unittest

class TestComponent(unittest.TestCase):
    def test_1(self):
        pass

if __name__ == '__main__':
    unittest.main()
```

##### Commands

`python3 -m unittest` runs all test classes whose names start with `Test` inside a `test_` file and executes the methods starting with `test` within it

You can combine it with other flags like:

- `-v` returns a verbose (more detailed) report of the tests that were run

### Pytest

Basic pytest test structure:

```python {"id":"01J06FA587V4VFM6RY4V18E606"}
import pytest

def test_1():
    pass
```

##### Commands

`pytest` finds all files `test\_\*.py` or `\*\_test.py` and runs all the functions starting with `test\_` and/or classes `Test\*` within them

You can combine it with other flags like:

- `-k 'pattern'` runs tests that follow a pattern
    
    example: `pytest order and not right`

- `-v` returns a verbose (more detailed) report of the tests that were run

##### Markers

Markers "mark" a function and give it more functionality. You apply them to functions like decorators.

- `@pytest.mark.parametrize(argnames : str, argvalues : list)` enables parametrization of arguments for a test function

|| Argnames | Argvalues |
| --- | --- | --- |
| One argument | "arg1" | \["value1", "value2", "value3"\] |
| Multiple arguments | "arg1,arg2" | \[(arg1_val1, arg2_val1), (arg1_val2, arg2_val2), (arg1_val3, arg2_val3)\] |

- `@pytest.mark.skipif(condition, reason : str )` skips the function if the condition returns `True`

##### Functions and keywords

Here are the functions and keywords we used today:

- `pytest.fail(reason : str)` forces the test to fail

- `assert` checks the condition that follows; if it returns `True`, the test passes, otherwise it fails

### Resources

a.k.a. all the resources from which I studied (not everything was discussed during the tutoring session).

- [Class notes](https://github.com/fbw-p24-e01-assignments/live_code/tree/main/PYTHON/2.14_TESTING)
- [_Unittest_ on pythontutorial.net](https://www.pythontutorial.net/python-unit-testing/python-unittest/)
- [_Functional testing_ on Wikipedia](https://en.wikipedia.org/wiki/Functional_testing)
- [_Unittest coverage_ on pythontutorial.net](https://www.pythontutorial.net/python-unit-testing/python-unittest-coverage/)
- [_Get started_ on Pytest documentation](https://docs.pytest.org/en/stable/getting-started.html)
- [_How to invoke Pytest_ on Pytest documentation](https://docs.pytest.org/en/stable/how-to/usage.html)
- [_Fixtures_ on Pytest documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [_How to mark test functions with attributes_ on Pytest documentation](https://docs.pytest.org/en/stable/how-to/mark.html)
- [_References_ on Pytest documentation](https://docs.pytest.org/en/stable/reference/reference.html)
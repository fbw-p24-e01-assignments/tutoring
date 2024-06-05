# Loops

### Making the for loop explicit

Python's

`for i in range(n)`

is shorthand for

`for {i = 0; i < n; i += 1}`

- start: *i* starts from 0
- condition: while *i* is less than *n*
- at the end of every loop: increase *i* by 1 

### Loops with iterables

`for i in [10, 15, 20]`

- 1st iteration: *i* is 10
- 2nd iteration: *i* is 15
- 3rd iteration: *i* is 20

# Our Live Code

The exercise on [HackerRank](https://www.hackerrank.com/challenges/python-loops/problem).

### Task

The provided code stub reads and integer, $n$, from STDIN. For all non-negative integers $i < n$, print $i²$. 

### Our solution

```python {"id":"01HZMPPQ1C23DA8KZRNMRGQJM8"}
def loop(n):
    '''what do we need that we don't have yet'''
    for i in range(n): # 0 to n - 1
        print(i ** 2)

'''code stub:'''
if __name__ == '__main__':
    n = int(input()) # size of list
    loop(n)
```
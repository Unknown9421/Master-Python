"""
    How to merge dictionaries in Python 2.x and 3.x
    https://realpython.com/python-tricks/
"""

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
z = {**x, **y}
# z = dict(x, **y)

print(z)
#main.py

from get_int import *
from get_float import *
if __name__ == '__main__':
    x = get_float("x: ")
    y = get_int("y: ")
    z = x**y

    print(z)
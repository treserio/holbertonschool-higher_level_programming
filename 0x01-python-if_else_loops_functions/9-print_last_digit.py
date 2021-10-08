#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        return number % 10 if print(number % 10, end="") is None else None
    else:
        return -number % 10 if print(-number % 10, end="") is None else None

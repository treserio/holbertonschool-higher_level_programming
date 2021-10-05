#!/usr/bin/python3
def roman_to_int(roman_string):
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = int(0)
    if roman_string:
        j = iter(list(roman_string[1:]))
        for i in roman_string:
            k = next(j, i)
            if vals[i] < vals[k]:
                total -= vals[i]
            else:
                total += vals[i]

    return total

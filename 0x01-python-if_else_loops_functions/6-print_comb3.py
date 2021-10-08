#!/usr/bin/python3
r = range(10)
print(', '.join("{}{}".format(i, j) for i in r for j in r if j > i))

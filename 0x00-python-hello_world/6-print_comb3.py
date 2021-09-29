#!/usr/bin/python3
print(', '.join("{}{}".format(i, j) for i in range(10) for j in range(10) if j > i))

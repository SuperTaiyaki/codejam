#!/usr/bin/python3

import math

# given a fraction, how many times does the denominator have to be doubled to
# find a 1/1...?

# (1/2, 1/2)
# (1/4, 1/4, 1/4, 1/4)....

# So... log2 it?

# 40 generations... ???
# 

def debug(*args, **kwargs):
    print(*args, **kwargs)
    pass

cases = int(input())

for case in range (1, cases + 1):

    (num, den) = [int(x) for x in input().split("/")]
    test = num / den

    step = 1
    frac = 0.5
    impossible = False

    while frac > test:
        step += 1
        frac /= 2
        if step > 39:
            impossible = True
    if impossible: 
        print("Case #%s: %s" % (case, "impossible"))
    else:
        print("Case #%s: %s" % (case, step))


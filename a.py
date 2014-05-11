#!/usr/bin/python3

import math
import fractions

# given a fraction, how many times does the denominator have to be doubled to
# find a 1/1...?

# g1: (1/2, 1/2)
# g2: (1/4, 1/4, 1/4, 1/4)....
# g40: (1/2^40...)

# So... log2 it?

# 40 generations... ???
# Soo... her ancestors are at most 2^40 bits
# So... if the value of her ancestry can't be expressed as a sum of (1/2^40)
# it's not valid
# It's a divisibility test!


def debug(*args, **kwargs):
    print(*args, **kwargs)
    pass

cases = int(input())

for case in range (1, cases + 1):

    (num, den) = [int(x) for x in input().split("/")]
    test = fractions.Fraction(num, den)

    step = 1
    frac = fractions.Fraction(1, 2)
    impossible = False
    limit = fractions.Fraction(1, 1099511627776) # 2^40

    if (test/limit).denominator != 1:
        print("Case #%s: %s" % (case, "impossible"))
        continue

    while frac > test:
        step += 1
        frac /= 2
        if step > 40:
            impossible = True
    if impossible: 
        print("Case #%s: %s" % (case, "impossible"))
    else:
        print("Case #%s: %s" % (case, step))


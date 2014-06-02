#!/usr/bin/python3

import bisect

# 1: Maximum 2 files
# 2: never split file

# Strategy: Take largest file
# Find largest file to pair it with... done?

# Ohh.... should probably be pairing to minimize wasted space instead of just
# the biggest file...?

def debug(*args, **kwargs):
    #print(*args, **kwargs)
    pass

cases = int(input())

for case in range (1, cases + 1):

    (_, capacity) = [int(x) for x in input().split()]
    files = [int(x) for x in input().split()]
    files.sort()
    debug("Disc size: %s" % capacity)
    debug(files)

    discs = 0

    while files:
        debug("-----------------")
        discs += 1
        largest = files.pop()
        debug("Doing %s" % largest)
        if not files:
            break

        # binary search for the number closest to remain

        remain = capacity - largest

        idx = bisect.bisect_right(files, remain)
        debug("Entry %s" % idx)
        #if idx > len(files):
        #    debug("No match?")
        #else:
        if idx:
            found = files.pop(idx - 1)
            debug("Removing %i" % found)
        else:
            debug("No match?")
    print("Case #%s: %s" % (case, discs))
    

#!/usr/bin/python3

import copy

# Slow approach: count swaps to move the lowest item to the front
#   Then iterate algorithm with the remainder of the list
# Also move the highest item to the front
# -> Then number of swaps to finish reverse-sorting the list

# wait that's not right
# Start by finding where the list stops being ascending, can probably cut off
# the section before that
# Count swaps to pull in the... next highest number?
# Compare to efficiency of changing to reducing at this point?

# What's the optimal efficiency of the swappy sort? Is it equivalent to bubble
# sort?
# Hrm... probably:
# Scan out the lowest element
# Swap into place
# Continue
#   Can this be done _without_ actually stepping it?
#      Yeah, everything else just gets moved up one

# 5 4 3 2
# 3 swaps to move 2 to the front, remainder 5 4 3

# should be possible to do some sort of optimization based on the highest in the
# list

# bruteforce: sort all ascending
# Sort all descending
# Taking just the front and reordering in-place won't find the optimal

# So... any given number can have 2 possible places in the string - the
# ascending, or the descending
# Should measure the distance to both, and find the nearest...

# If only I figured this out 3 minutes faster...

def debug(*args, **kwargs):
    # print(*args, **kwargs)
    pass

cases = int(input())

def downsort(lll):
    """ Number of swaps to sort remaining items descending"""
    swaps = 0
    while lll:
        lowest = max(lll)
        idx = lll.index(lowest)
        swaps += idx
        lll.pop(idx)
    return swaps

for case in range (1, cases + 1):

    input() # Number of elems
    elems = [int(x) for x in input().split()]
    debug(elems)

    nums = sorted(elems)
    nums.reverse()
    swaps = 0

    while(elems):
        next = nums.pop()
        idx = elems.index(next)
        debug("Searching for %s" % next)
        b = len(elems) - idx - 1
        debug("%s vs %s" % (idx, b))
        swaps += min([idx, b])
        elems.pop(idx)

    print("Case #%s: %s" % (case, swaps))
    

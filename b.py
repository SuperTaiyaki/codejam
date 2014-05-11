#!/usr/bin/python3

import copy
import math
import itertools

# Small case: up to 10!, bruteforce time!

# hrm... aa aa bc c is valid, abc bcd is not - the lone 'c' makes it impossible!
# so... ordering is fixed unless:
#   -there are multiple continuous single-char blocks (aa aaa)
#   -there are disconnected segments (aa aa bb bb)
# So... generate outwards and multiply out the possibilities?


# Large case: probably build up from the back, memo-ize...

# Crunch any repeated chars
# group all one-char blocks (i.e. a a a becomes a single a, with 8 arrangements)
# Find anything floating (can be placed anywhere), include in a different array
#   later these can be permuted freely
# Find anything locked, jam together
#   Worst case is ab b bc at this stage
#   And the b could have, say, 8 permutations, so we can reduce this to an 'ac'
#   block with 8 permutations (and mark 'b' as locked - if there are any
#   outside, it's impossible)
#       Actual algorithm: Take a block, append onto the end until a free set is
#       formed

# Blowout case:
# 100 factorial...? ok, 26 factorial because it'll be running through the list
# repeatedly, only updating the last element...
# Which isn't even all that bad, because it's circular... uhh...
# is ab bc cd .... the worst case then?
# Or the reverse?

def debug(*args, **kwargs):
    # print(*args, **kwargs)
    pass

cases = int(input())

for case in range (1, cases + 1):
    debug("===========================main start=================")
    nblocks = int(input())
    blocks = input().split()
    cblocks = []
    charset = set()
    # Pre-process, crunch all contiguous strings of chars
    for block in blocks:
        out = ""
        last = ''
        for char in block:
            if char == last:
                continue
            out += char
            last = char
            charset.add(char)
        cblocks.append(out)

    debug(cblocks)

    pblocks = []
    # Shrink out single-char blocks
    for c in charset:
        count = cblocks.count(str(c))
        if count > 0:
            pblocks.append((str(c), math.factorial(count)))
    for block in cblocks:
        if len(block) == 1:
            continue
        pblocks.append((block, 1))

    debug(pblocks)
    locked = set()
    floating = []
    impossible = False

    while pblocks:
        debug("--------ITER START------------")
        debug("pblocks:  %s" % pblocks)
        debug("floating: %s" % floating)
        debug("Locked: %s" % locked)
        (block, count) =  pblocks.pop(0)

        debug("Evaluating %s" % block)
        #for char in block:
            #if char in locked:
            #    debug("Character overlap; aborting")
            #    impossible = True
            #    break
        if impossible:
            break
        # (block, count) =
        segment = block

        def ffirst(part):
            global count # Outside is not in a def
            if part[0] == segment[0] or part[0] == segment[-1]:
                count *= part[1]# TODO: Is this actually a += ?
                debug("Merging %s to %s" % (part[0], segment))
                return False
            return True
        pblocks2 = list(filter(ffirst, pblocks))
        pblocks = pblocks2 # Just in case...?
        
        matched = False
        for i, (chars, perms) in enumerate(pblocks):
            # Block, not segment! Don't die because we can chain, do that later
            if block[-1] != chars[0]:
                continue
            if matched is not False:
                # double match. Explode!
                debug("Double match!")
                impossible = True
                break
            debug("Extending %s with %s" % (segment, chars))

            # we have X permutations on the current block
            # Next segment has Y permutations
            # So... multiply them together

            if len(segment) > 1:
                segment += chars
            else:
                segment = chars
            debug("New segment: %s" % segment)
            count *= perms
            matched = i
        if impossible:
            break
        if matched is not False:
            del pblocks[matched]
            if len(segment) > 3:
                debug("Locking %s" % segment[1:-1])
                for char in segment[1:-1]:
                    locked.add(char)
            pblocks.append((segment, count))
        else: 
            # So, nothing to append onto the tail
            # If nothing can append to the head either, eject this block as
            # floating

            # Single characters matching the lead have already been absorbed
            matched = 0
            for chars, _ in pblocks:
                if chars[-1] == segment[0]:
                    matched += 1
            debug("Head matches: %s" % matched)
            if matched == 0:
                if len(segment) > 2 or len(segment) == 1:

                    debug("Locking %s" % segment)
                    for char in segment:
                        locked.add(char)
                debug("No head matches for %s; floating" % segment)
                floating.append((segment, count))
            elif matched > 1:
                impossible = True
                break
            else:
                # Exactly one match, put it back in the queue
                pblocks.append((segment, count))

    debug("Final pblocks: %s" % pblocks)
    debug("Final floating: %s" % floating)

    # Check for illegal condition, where characters are non-contiguous
    chars = set()
    last = ''
    for block in floating:
        last = ''
        for char in block[0]:
            if last == char:
                continue
            if char in chars:
                impossible = True
                debug("Found illegal char %s in floating" % char)
                break
            else:
                chars.add(char)
                last = char
        if impossible:
            break

    if impossible: 
        print("Case #%s: %s" % (case, 0))
        continue

    # if len(pblocks) == 1:
    #     print("Case #%s: %s" % (case, pblocks[0][1]))
    # else:
    #     print("Case #%s: %s" % (case, 0))
    if len(pblocks) > 0:
        print("ERRORRRRRRRRRRRRR: PBLOCKS!")
    else:
        # TODO: mod 1,000,000,007.
        multiplier = 1
        for _, num in floating:
            multiplier *= num
        multiplier *= math.factorial(len(floating))
        print("Case #%s: %s" % (case, multiplier % 1000000007))

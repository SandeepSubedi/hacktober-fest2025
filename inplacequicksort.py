#!/usr/bin/env python3
import random, sys, argparse

def _partition(a, lo, hi):
    p = a[random.randint(lo, hi)]
    i, j = lo - 1, hi + 1
    while True:
        i += 1
        while a[i] < p: i += 1
        j -= 1
        while a[j] > p: j -= 1
        if i >= j: return j
        a[i], a[j] = a[j], a[i]

def quicksort(a):
    if len(a) < 2: return a
    stack = [(0, len(a)-1)]
    while stack:
        lo, hi = stack.pop()
        while lo < hi:
            p = _partition(a, lo, hi)
            # recurse into smaller part; loop over larger (tail-call elim)
            if p - lo < hi - (p+1):
                stack.append((p+1, hi)); hi = p
            else:
                stack.append((lo, p)); lo = p+1
    return a

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("nums", nargs="*", type=int, help="numbers to sort")
    ns = ap.parse_args().nums or [5, -2, 9, 1, 1, 7, 3, 0]
    print(quicksort(ns))

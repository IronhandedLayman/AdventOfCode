#!/usr/bin/env python3

from collections import defaultdict

def part1(inp):
    return sumAcrossPackagesFile(inp, calcArea)

def part2(inp):
    return sumAcrossPackagesFile(inp, calcRibbon)

def sumAcrossPackagesFile(inp, fn):
    ans = 0
    for pkg in inp.split("\n"):
        dims = [int(x) for x in pkg.split("x") if len(x)>0]
        if len(dims)==3:
            ans += fn(dims[0],dims[1],dims[2])
    return ans

def calcArea(l, w, h):
    side1 = l*w
    side2 = w*h
    side3 = l*h
    return 2*(side1 + side2 + side3) + min(side1, side2, side3)

def calcRibbon(l, w, h):
    extra = l * w * h
    shortPerim = 2 * (l + w + h - max(l,w,h))
    return shortPerim + extra

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

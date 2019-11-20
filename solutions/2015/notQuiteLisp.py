#!/usr/bin/env python3

from collections import defaultdict


def part1(inp):
    floorKey = defaultdict(int)
    floorKey['(']=1 
    floorKey[')']=-1 
    return sum(floorKey[x] for x in inp)

def part2(inp):
    floorKey = defaultdict(int)
    floorKey['(']=1 
    floorKey[')']=-1 
    currentFloor = 0
    for p,x in enumerate(inp):
        currentFloor+=floorKey[x]
        if currentFloor < 0:
            return p+1
    return -1        

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

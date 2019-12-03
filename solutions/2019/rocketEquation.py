#!/usr/bin/env python3
import hashlib

def part1(inp):
    ans = 0
    for x in inp.split("\n"):
        if len(x)>0:
            ans += fuelCounter(int(x))
    return ans

def part2(inp):
    ans = 0
    for x in inp.split("\n"):
        if len(x)>0:
            ans += realFuelCounter(int(x))
    return ans

def fuelCounter(mass):
    return (mass // 3) - 2

def realFuelCounter(mass):
    if mass < 9:
        return 0
    req = (mass // 3) - 2
    return req + realFuelCounter(req)

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

def testFuelCounter():
    testCases = {
            "12":2,
            "14":2,
            "1969":654,
            "100756":33583,
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part1(tc)))

def testRealFuelCounter():
    testCases = {
            "14":2,
            "1969":966,
            "100756":50346,
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part2(tc)))

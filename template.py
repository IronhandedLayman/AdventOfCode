#!/usr/bin/env python3
import hashlib

def part1(inp):
    pass

def part2(inp):
    pass

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

def testPart1():
    testCases = {
            "input":"expectedOutput",
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part1(tc)))

def testPart2():
    testCases = {
            "input":"expectedOutput",
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part2(tc)))

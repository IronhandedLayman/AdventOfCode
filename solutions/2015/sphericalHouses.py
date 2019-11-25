#!/usr/bin/env python3

from collections import defaultdict

def dirMap():
    ans = defaultdict(lambda: (0,0))
    ans['^'] = (0,1)
    ans['v'] = (0,-1)
    ans['<'] = (1,0)
    ans['>'] = (-1,0)
    return ans

def part1(inp):
    dm = dirMap()
    allHouses = set()
    sledLoc = (0,0)
    allHouses.add(sledLoc)
    for d in inp:
        dd = dm[d]
        sledLoc = (sledLoc[0]+dd[0], sledLoc[1]+dd[1]) 
        allHouses.add(sledLoc)
    return len(allHouses)

def part2(inp):
    dm = dirMap()
    allHouses = set()
    santaSledLoc = (0,0)
    roboSantaSledLoc = (0,0)
    allHouses.add(santaSledLoc)
    santaTurn = True
    for d in inp:
        dd = dm[d]
        if santaTurn:
            santaSledLoc = (santaSledLoc[0]+dd[0], santaSledLoc[1]+dd[1]) 
            allHouses.add(santaSledLoc)
        else:
            roboSantaSledLoc = (roboSantaSledLoc[0]+dd[0], roboSantaSledLoc[1]+dd[1]) 
            allHouses.add(roboSantaSledLoc)
        santaTurn = not santaTurn
    return len(allHouses)

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

def testPart1():
    testCases = {
            ">": 2,
            "^>v<":4,
            "^v^v^v^v^v":2,
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part1(tc)))

def testPart2():
    testCases = {
            "^v":3,
            "^>v<":3,
            "^v^v^v^v^v":11,
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part2(tc)))

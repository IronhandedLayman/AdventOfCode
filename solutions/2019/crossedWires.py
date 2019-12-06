#!/usr/bin/env python3
import hashlib

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def manDist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def manOrg(self):
        return self.manDist(Point(0,0))

    def __str__(self):
        return "({0.x},{0.y})".format(self)

    def __repr__(self):
        return "({0.x},{0.y})".format(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))


ORIGIN = Point(0,0)

def part1(inp):
    t1, t2 = [genTrace(x) for x in inp.split("\n") if len(x)>0]
    return min(p1.manOrg() for p1 in t1[0].intersection(t2[0]))

def part2(inp):
    t1, t2 = [genTrace(x) for x in inp.split("\n") if len(x)>0]
    return min(tr1 + tr2 for x in t1[0].intersection(t2[0]) for tr1, tr2 in [(t1[1][x],t2[1][x])])

def genTrace(inpline):
    ans = set()
    ans2 = {}
    at = Point(0,0)
    tsf = 0
    for c in inpline.split(","):
        if len(c)==0:
            continue
        d=c[0]
        dist=int(c[1:])
        if d=="U":
            for i in range(dist):
                at = Point(at.x,at.y+1)
                ans.add(at)
                tsf += 1
                if at not in ans2:
                    ans2[at] = tsf
        elif d=="D":
            for i in range(dist):
                at = Point(at.x,at.y-1)
                ans.add(at)
                tsf += 1
                if at not in ans2:
                    ans2[at] = tsf
        elif d=="L":
            for i in range(dist):
                at = Point(at.x+1,at.y)
                ans.add(at)
                tsf += 1
                if at not in ans2:
                    ans2[at] = tsf
        elif d=="R":
            for i in range(dist):
                at = Point(at.x-1,at.y)
                ans.add(at)
                tsf += 1
                if at not in ans2:
                    ans2[at] = tsf
    return (ans,ans2)

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

def testPart1():
    testCases = {
            "R8,U5,L5,D3\nU7,R6,D4,L4":6,
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83":159,
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7":135,
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part1(tc)))

def testPart2():
    testCases = {
            "R8,U5,L5,D3\nU7,R6,D4,L4":30,
            "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83":610,
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7":410,
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part2(tc)))

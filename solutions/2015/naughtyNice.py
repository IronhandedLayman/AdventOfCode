#!/usr/bin/env python3
import hashlib

def part1(inp):
    ans = 0
    for x in inp.split("\n"):
        if niceStringPart1(x):
            ans+=1
    return ans

def part2(inp):
    ans = 0
    for x in inp.split("\n"):
        if is_really_nice(x):
            print("[X] {}".format(x))
            ans+=1
        else:
            print("[ ] {}".format(x))
    return ans

def part3(inp):
    ans = 0
    for x in inp.split("\n"):
        if is_really_nice(x) and niceStringPart2(x):
            print("[X] {}".format(x))
            ans+=1
        elif is_really_nice(x) and not niceStringPart2(x):
            print("[ ] {}".format(x))
    return ans

def niceStringPart1(judged):
    vowels = "aeiou"
    forbiddenDigrams="ab,cd,pq,xy"
    vowelCount = 0
    lastLet = None
    doubler = False
    for c in judged:
        if c in vowels:
            vowelCount+=1
        if lastLet is not None:
            if c == lastLet:
                doubler = True
            if lastLet+c in forbiddenDigrams:
                return False
        lastLet = c    
    if vowelCount<3:
        return False
    if not doubler:
        return False
    return True

def niceStringPart2(judged):
    lastLet = None
    twoBack = None
    pairRepeat = False
    abaRepeat = False
    bigramStore = set()
    for x in judged:
        # print(x, end=":")
        bigram1 = None #Bigram with one letter back
        bigram2 = None #Bigram with two letters back 
        if lastLet is not None:
            bigram1 = lastLet+x
            # print(lastLet+"|"+bigram1,end=",")
            if twoBack is not None:
                bigram2 = twoBack+lastLet
                # print(twoBack+"|"+bigram2,end=",")
                if twoBack == x:
                    abaRepeat = True
                    # print("[abaRepeat!]",end="")
        if bigram1 != bigram2 or bigram2 is None:
            if bigram1 not in bigramStore:
                bigramStore.add(bigram1)
            else:
                pairRepeat = True
                # print("[pairRepeat!]",end="")
        twoBack = lastLet
        lastLet = x
        # print()
    print("{}::pairRepeat={},abaRepeat={}".format(judged,pairRepeat,abaRepeat))
    return pairRepeat and abaRepeat

def is_really_nice(s):
    first = False
    for i in range(len(s) - 3):
        sub = s[i: i + 2]
        if sub in s[i + 2:]:
            first = True
            print("{} is really nice and repeats with {}".format(s, sub))
            break
    if not first:
        return False
    second = False
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            second = True
            break
    return second

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

def testNiceStringPart1():
    testCases = {
            "ugknbfddgicrmopn":True,
            "aaa":True,
            "jchzalrnumimnmhp":False,
            "haegwjzuvuyypxyu":False,
            "dvszwmarrgswjxmb":False
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,niceStringPart1(tc)))

def testNiceStringPart2():
    testCases = {
            "qjhvhtzxzqqjkmpb":True,
            "xxyxx":True,
            "uurcxstgmygtbstg":False,
            "ieodomkazucvgmuy":False,
            "abcde":False,
            "aaabaaa": True 
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,niceStringPart2(tc)))

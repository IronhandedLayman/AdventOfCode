#!/usr/bin/env python3
import hashlib

OP_ADD = 1
OP_MULT = 2
OP_HALT = 99

def part1(inp):
    pc = IntCoder(inp)
    return pc.runCommand(12,2)

def part2(inp):
    pc = IntCoder(inp)
    noun = 0
    target = 19690720
    while True:
        for verb in range(0,noun+1):
            if pc.runCommand(noun,verb)==target:
                return (noun,verb)
            elif pc.runCommand(verb,noun)==target:
                return (verb,noun)
        noun+=1

class IntCoder():
    def __init__(self, inp):
        self.rom = [int(x) for x in inp.split(",") if len(x)>0] + [0,0,0,0]
        self.codes = [int(x) for x in inp.split(",") if len(x)>0] + [0,0,0,0]
        self.pc = 0
        self.halted = False

    def reset(self):
        for i,x in enumerate(self.rom):
            self.codes[i]=x
        self.pc=0
        self.halted=False

    def runCommand(self, noun, verb):
        self.reset()
        self.set(1,noun)
        self.set(2,verb)
        while not self.halted:
            self.step()
        return self.get(0)

    def set(self, addr, val):
        self.codes[addr] = val

    def get(self, addr):
        return self.codes[addr]

    def getRegs(self):
        return {
                "pc":self.pc,
                "halted": self.halted,
                }
    
    def step(self):
        print("command:" + ",".join(str(x) for x in self.codes[self.pc:self.pc+4]))
        if self.halted:
            return False
        curpc = self.pc
        op, a, b, c = self.codes[curpc:curpc+4]
        if op == OP_ADD:
            self.codes[c] = self.codes[a] + self.codes[b]
            self.pc = curpc+4
        elif op == OP_MULT:
            self.codes[c] = self.codes[a] * self.codes[b]
            self.pc = curpc+4
        elif op == OP_HALT:
            self.halted = True
        else:
            print("UNRECOGNIZED OPCODE")
            self.halted = True #HCF


def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

def testPart1():
    testCases = {
            "1,0,0,0,99": 2,
            "2,3,0,3,99": 2,
            "2,4,4,5,99,0": 2,
            "1,1,1,4,99,5,6,0,99": 30
            }
    for tc,a in testCases.items():
        print("Case [{}]: expected: {}, got: {}\n".format(tc,a,part1(tc)))

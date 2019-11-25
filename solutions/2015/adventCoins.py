#!/usr/bin/env python3
import hashlib

def part1(inp):
    return adventCoinNonce(inp,"00000")

def part2(inp):
    return adventCoinNonce(inp,"000000")

def adventCoinNonce(inp, difficulty):
    ans = 0
    while (ans < 4000000000000):
        ans = ans + 1
        m = hashlib.md5()
        key = inp+str(ans)
        m.update(key.encode())
        if m.hexdigest().startswith(difficulty):
            return ans
    return -1

def fromFile(fn,func):
    with open(fn,'r') as f:
        cin = f.read()
        return func(cin)

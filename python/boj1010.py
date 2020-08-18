import sys
import math
inputLine = sys.stdin.readline

def nCr(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

T = int(input())
for i in range(T):
    N,M  = map(int,input().split(' '))
    print(int(nCr(M,N)))

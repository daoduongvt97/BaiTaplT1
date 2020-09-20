import math
import operator as op
from functools import reduce
def nCr(n,r):
    r = min(r, n-r)
    number = reduce(op.mul, range(n, n-r, -1),1)
    denom = reduce(op.mul, range(1,r+1),1)
    return number//denom
def prop(n, p, r):
    return nCr(n+r-1, n)*(p**r)*((1-p)**n)
def infoMeasure(n, p, r):
    return -math.log(prop(n,p,r))
def sumProb(N, p, r):
    sum = 0.0
    for i in range(1,N+1):
        sum += prop(i, p, r)
    return sum
def approxEntropy(N, p, r):
    result = 0.0
    for i in range(1,N+1):
        result += prop(i,p, r)*infoMeasure(i, p, r)
    return result

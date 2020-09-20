import math
import operator as op
from functools import reduce
def nCr(n,r):
    r = min(r, n-r)
    number = reduce(op.mul, range(n, n-r, -1),1)
    denom = reduce(op.mul, range(1,r+1),1)
    return number//denom
def prop(n, p, N):
    return nCr(N, n)*(p**n)*((1-p)**(N-n))
def infoMeasure(n, p, N):
    return -math.log(prop(n,p,N))
def sumProb(N, p):
    sum = 0.0
    for i in range(1,N+1):
        sum += prop(i, p, N)
    return sum
def approxEntropy(N, p):
    result = 0.0
    for i in range(1,N+1):
        result += prop(i,p, N)*infoMeasure(i, p, N)
    return result
print(nCr(5,2))
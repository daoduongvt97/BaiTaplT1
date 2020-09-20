import math
def prop(n, p):
    return p**(n-1)*(1-p)
def infoMeasure(n,p):
    return -math.log(prop(n,p))
def sumProb(N,p):
    sum = 0.0
    for i in range(1,N+1):
        sum += prop(i, p)
    return sum
def approxEntropy(N,p):
    result = 0.0
    for i in range(1,N+1):
        result += prop(i,p)*infoMeasure(i, p)
    return result

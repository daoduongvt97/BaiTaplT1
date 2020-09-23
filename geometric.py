import math
def prop(n, p):
    return p**(n-1)*(1-p)
def infoMeasure(n,p):
    return -math.log(prop(n,p),2)
def sumProb(N,p):
    """
        sumProb(10,0.5) = 0.9990234375,
        sumProb(100,0.5) = sumProb(100,0.5) = 1.0
        => tổng xác suất của phân bố geometric tiến dần về 1
    """
    sum = 0.0
    for i in range(1,N+1):
        sum += prop(i, p)
    return sum
def approxEntropy(N,p):
    result = 0.0
    for i in range(1,N+1):
        result += prop(i,p)*infoMeasure(i, p)
    return result

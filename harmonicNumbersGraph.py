import pylab
import math

def harm(x, harmSumUntil = {}):
    if x <= 0:
        return 0
    if x in harmSumUntil:
        return harmSumUntil[x]
    harmSumUntil[x] = harm(x-1) + 1./x
    return harmSumUntil[x]
    
    #Non-recursive and non-memoized form: sum([1./y for y in range(1, x+1)])
    

pylab.plot([harm(x) for x in range(1, 10000)], label="harmonic")
pylab.plot([math.log(x) for x in range(1, 10000)], label="log")
pylab.plot([x**(1/3.) for x in range(1, 10000)], label="**(1/.3)")

pylab.legend()
pylab.show()


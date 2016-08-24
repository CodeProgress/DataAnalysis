import pylab
import random

num_positive = []
for step in range(20):
    count = 0
    offset = 1 - (step * 3.5**-5)
    print offset
    for trial in xrange(100):
        # data = []
        price = 0
        price = sum(random.random() * 2 - offset for _ in xrange(10000))
        # for i in xrange(10000):
        #     price += random.random()*2 - .9999
            # data.append(price)
        if price > 0:
            count += 1
    num_positive.append(count)

print count
pylab.plot(num_positive)
pylab.show()

# pylab.plot(data)
# pylab.show()

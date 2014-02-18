import itertools
import collections
import pylab




def plot_unique_sums(nums = [1,2,3,4,5,6,7,8,9,10]):
    """plot the unique sums achieved by adding the numbers in num 
    in all possible combinations, including with replacement.
    nums: List of ints
    """
    count = collections.Counter()

    limit = len(nums)

    ys = [x for x in nums]
    
    colors = pylab.cm.rainbow(pylab.linspace(0, 1, len(ys)))
    place  = 0
    
    for i in range(1, limit+1):
        pairs = itertools.combinations_with_replacement(nums, i)
        for p in pairs:
            count[sum(p)] += 1
        
        pylab.scatter(count.values(), 
                      count.keys(), 
                      color = colors[place], 
                      label = str(i)
                      )
        place += 1
        place %= limit

    pylab.xlabel("Number of Combinations Totaling Sum")
    pylab.ylabel("Value of Sum")
    pylab.legend()
    pylab.show()

plot_unique_sums()

"""
project euler problem 5
lowest number with factors from 1 to 20

What we really need is the shortest list of numbers from 1 to 20
which contain all of the factors. That list is: 5,7,9,11,13,16,17,19
How do we derive this list? I think we need all of the factors of all
the numbers, then we need to sort out which lowest set of numbers
contains all of the factors.
"""

# factors will hold the factors of each number from 2 to 20.
factors=[[],[]]
for i in range(2,21):
    factors.append([])
    for j in range(2,i):
        if i % j == 0:
            factors[i].append(j)
            # add a factor for perfect squares. They're special in that we
            # need to make sure the square is either a factor of another
            # number, or is accounted for in our list.
            if i/j == j:
                factors[i].append(j)

for k in range(2,len(factors)):
    print(k, factors[k])

common_factors=[]

for i in range(20,1,-1):
    factorsflag=0
    for j in factors:
        

"""
project euler problem 1
sum of all multiples of 3 and 5 below 1000
"""

def mod3_5(n):
    return n%3==0 or n%5==0

# filter 0-1000 to find if the number is divisible by 3 or 5.
# filter returns an iterable object, so we "list" it and then
# sum the list.
s=sum(list(filter(mod3_5,range(1000))))

print (s)


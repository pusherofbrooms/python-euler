"""
project euler problem 16
sum of all of the digits in 2**1000
"""

num=str(2**1000)

# treating the num string as a vector to iterate over
s=sum(int(i) for i in num)

print(s)

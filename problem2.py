"""
project euler problem 2
sum of the even fibonacci numbers less than 4000001
"""

old_sum=1
new_sum=2
tot=2

while new_sum <= 4000000:
    x = new_sum;
    new_sum = new_sum + old_sum
    old_sum = x
    if new_sum % 2 == 0:
        tot += new_sum

print(tot)

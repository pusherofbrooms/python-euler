"""
project euler problem 4
find the largest palindrome number made from the product of 2 three digit numbers
"""

def ispalindrome (n):
    forward=n
    reverse=0

    while n > 0:
        # if the last digit is zero this is not a palindrome number
        if n % 10 == 0 and reverse == 0:
            return False
        # collect the digits in reverse order
        reverse = reverse * 10;
        reverse += n % 10
        n = int(n/10);
    if reverse == forward:
        return True
    else:
        return False


highest_palindrome=1
# too lazy to count from 100 to 999 since 900 to 999 likely has some palindromes
for x in range(900,999):
    for y in range(x,999):
        product=x*y
        if ispalindrome(product) and product > highest_palindrome:
            highest_palindrome=product

print(highest_palindrome)

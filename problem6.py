"""
Project euler problem 6
The difference of the sum of squares from the square of sums of numbers from 1 to 100 (natural numbers)
"""

lastnum=100

sumofsquares=sum(i**2 for i in range(1,lastnum+1))
squareofsum=sum(range(1,lastnum+1))**2

print (squareofsum - sumofsquares)

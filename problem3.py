"""
project euler problem 3
the largest prime factor of 600851475143
If you want to use #!/something/python above, be sure to change
argnum to 1.
"""

import sys

argnum=2

def lgst_prime_factor(n):
    largest_fsctor=1
    factor_candidate=2

    while n != 1:
        while n % factor_candidate == 0:
            largest_factor = factor_candidate
            n = n / factor_candidate

        factor_candidate+=1

    return largest_factor

def usage():
    print("""usage:
python problem3.py 600851475143
to solve project euler problem 3""")
    

if len(sys.argv) > 1:
    n=sys.argv[1]
    if n.isnumeric():
        print(lgst_prime_factor(int(n)))
    else:
        usage()

else:
    usage()
    
    

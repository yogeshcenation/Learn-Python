#!/home/yogesh-s/PycharmProjects/Python Programming/Introduction/GCD Using Euclids Algo.py
"""
    File name: GCD Using Euclid's Algo.py.py
    Description: Method Definition to find GCD of 2 numbers using Euclid's Algorithm.
    Author: Yogesh.S
    Date created: 01/18/2022
    Date last modified: 01/18/2022
    Python Version: 3.8
"""

"""
 Lets consider the case :
    1. Suppose d divides both m and n, and m > n ,
        then m = ad and n= bd .
        So, m - n = (ad - bd) => (a - b)* d .
        Then d , divides m - n as well!
    Therefore, gcd(m,n) = gcd(n, m -n)    
"""

"""    
 Algorithm :
    1. Consider  gcd(m,n) with m > n 
    2. If n % m ,return n,
       Otherwise,compute gcd(n. m-n) and return that value
"""


# Method Definition
def gcd(m, n):
    # Assume m >= n :
    if m < n:
        (m, n) = (n, m)

    if (m % n) == 0:
        return n
    else:
        diff = m - n
        # diff > n? Possible!
        return gcd(max(n, diff), min(n, diff))
    return n


"""
     We can reduce the statements by using while loop.
"""


# Method Definition
def gcd_method2(m, n):
    # Assume m >= n :
    if m < n:
        (m, n) = (n, m)

    while (m % n) != 0:
        diff = m - n
        # diff > n? Possible!
        (m, n) = (max(n, diff), min(n, diff))
    return n


"""    
 What to do to get even better algorithm ?:
    1. Suppose n does not divide m.
       Then, m = qn + r, where q -> quotient and r -> remainder.
       Now, Assume d divides both m and n.
       Then, m =ad and n = bd.
       So, ad = q(bd) + r.
"""

"""    
 Actual Improved Algorithm :
    1. Consider  gcd(m,n) with m > n 
    2. If n % m ,return n,
       Otherwise,let r = m % n
    3. Return gcd(n,r)
    
 Efficiency:
    1. The above(2nd) algorithm takes time proportional to the number of digits in m.
       
       If m is 1 billion, the naive algorithm takes billions of steps,
       whereas this Improved (Euclid's) algorithm takes tens of steps.
"""


# Method Definition
def gcd_euclid_algorithm(m, n):
    # Assume m >= n :
    if m < n:
        (m, n) = (n, m)

    if (m % n) == 0:
        return n
    else:
        return gcd_euclid_algorithm(n, m % n)  # m % n < n ,always


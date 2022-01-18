#!/home/yogesh-s/PycharmProjects/Python Programming/Introduction/Naive_GCD_Improvement.py
"""
    File name: Naive_GCD_Improvement.py
    Description: This is the Method Definition to find GCD of 2 numbers by using single list .
    Author: Yogesh.S
    Date created: 01/18/2022
    Date last modified: 01/18/2022
    Python Version: 3.8
"""

"""
 Improving Simple GCD.py :
    1. We scan from 1 to m to compute fm and again from 1 to n to compute fn.
    
    2. Why not to do a single scan from 1 to max(m,n) ? 
       => For each 1 in 1 to max(m,n), add i to fm, if i % m and add i to fn , if i % n

 Can we do Even Better ? :
    1. Why compute two lists and then compare to common factors cf? Do it in one shot
       => For each 1 in 1 to max(m,n), if i % m and i % n , then add i to cf.
       
    2. Actually, any common factors must be less than min(m,n)
       => For each i in 1 to min(m,n),if i % m and also i % n , then add i to cf
"""


# Method Definition
def gcd(m, n):
    cf = []
    for i in range(1, min(m, n) + 1):
        if (m % i) == 0 and (n % 1) == 0:
            cf.append(i)
    return cf[-1]

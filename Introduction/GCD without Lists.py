#!/home/yogesh-s/PycharmProjects/Python Programming/Introduction/GCD without Lists.py
"""
    File name: GCD without Lists.py
    Description: This is the Method Definition to find GCD of 2 numbers without using "Lists" .
    Author: Yogesh.S
    Date created: 01/18/2022
    Date last modified: 01/18/2022
    Python Version: 3.8
"""

"""
 Improving Naive_GCD_Improvement.py :
    Method 1:
       We only need the largest common factor.
       1 is always be a common factor.
       Each time we find a largest common factor, discard the prev one.
       Remember the largest common factor seen so far and return it.
       => mcrf -> Most recent common factor 
       
    Method 2:
       To find the largest common factor,start at the end and work backwards.
       Let i run from min(m,n) to 1 
       First common factor that we will find will be GCD!  
"""


# Method Definition for 1st way
def gcd_method_1(m, n):
    for i in range(1, min(m, n) + 1):
        if (m % i and n % i) == 0:
            mcrf = i
    return mcrf


# Method Definition for 2nd way
def gcd_method_2(m, n):
    i = min(m, n)

    while i > 0:
        if (m % i and n % i) == 0:
            return i
        else:
            i = i - 1

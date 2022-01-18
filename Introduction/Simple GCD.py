#!//home/yogesh-s/PycharmProjects/Python Programming/Introduction/Simple GCD.py
"""
    File name: Simple GCD.py
    Description: This is the Method Definition to find GCD of 2 numbers using simple algorithm.
    Author: Yogesh.S
    Date created: 01/18/2022
    Date last modified: 01/18/2022
    Python Version: 3.8
"""

"""
 An algorithm for gcd(m,n) :-
    1. Use fm,fn for list of factors of m,n respectively.
    2. For each i from 1 to m, add i to fm , if i divides m.
    3. For each j from 1 to n, add j to fn,if j divides n.
    4. Use cf for lost of common factors.
    5. For each f in fm, add f to cf , if f also appears in fn.
    6. Return largest (rightmost) value in cf.
"""


# Method Definition
def gcd(m, n):
    fm = []
    for i in range(1, m + 1):
        if (m % i) == 0:
            fm.append(i)

    fn = []
    for j in range(1, n + 1):
        if (n % j) == 0:
            fn.append(j)

    cf = []
    for f in fn:
        if f in fn:
            cf.append(f)

    return cf[-1]

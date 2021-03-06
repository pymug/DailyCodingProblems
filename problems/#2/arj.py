'''
[Author]

Abdur-Rahmaan Janhangeer

[Statement]

Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

a = [1, 2, 3, 4, 5]

def sumExcept1(a):
    def product(a):
        p = 1
        for i in a:
            p *= i
        return p
    s = []
    for i in a:
        s.append(product(a)/i)
    return s

def sumExcept2(a):
    s = []
    for i in a:
        product = 1
        for x in a:
            if x == i:
                continue
            product *= x
        s.append(product)
    return s

print(sumExcept1(a))
'''
[Author]

Abdur-Rahmaan Janhangeer

[Statement]

Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

# 1

a = [10, 15, 3, 7]
k = 17

def check1(a, k):
    for i1 in a:
        for i2 in a:
            if i1 != i2 and i1+i2 == k:
                return True
    return False

def check2(a, k):
    return bool([x for x in a for y in a if x+y == k])

assert check1(a, k) == True, 'oops1'
assert check2(a, k) == True, 'oops2'
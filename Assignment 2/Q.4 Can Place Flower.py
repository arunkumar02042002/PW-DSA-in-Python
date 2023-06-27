"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
"""

def canPlaceFlowers(flowerbed, n):

    x = len(flowerbed)
    pos = 0
    if x == 1 and flowerbed[0] == 0:
        pos += 1
        return pos >= n

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        pos += 1
        flowerbed[0] = 1

    if flowerbed[-1] == 0 and flowerbed[-2] == 0 and x > 2:
        pos += 1
        flowerbed[-1] = 1

    for i in range(1, x-1):
        if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            flowerbed[i] = 1
            pos += 1

    return pos >= n

flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))
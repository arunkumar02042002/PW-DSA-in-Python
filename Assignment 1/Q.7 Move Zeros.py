"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

"""

def moveZeroes(nums):
    n = len(nums)
    countzero = 0

    for i in range(n):
        if nums[i] != 0:
            nums[countzero] = nums[i]
            countzero += 1

    while countzero < n:
        nums[countzero] = 0
        countzero += 1

nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)
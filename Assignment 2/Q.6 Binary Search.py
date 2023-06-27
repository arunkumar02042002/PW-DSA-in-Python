"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4
"""

def search(nums, target):
    left = 0
    right = len(nums)- 1

    while(left <= right):
        middle = (left + right) // 2

        if nums[middle] > target:
            right = middle - 1

        elif nums[middle] < target:
            left = middle + 1

        else:
            return middle
    return -1

nums = [-1,0,3,5,9,12]
target = 9
print(target)
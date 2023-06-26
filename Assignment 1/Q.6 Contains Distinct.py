"""
💡 **Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true

"""

def containsDuplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

nums = [1, 2, 1, 3]
print(containsDuplicate(nums))
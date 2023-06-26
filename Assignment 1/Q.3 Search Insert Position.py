"""

💡 Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2

"""

def binary_search(nums, l, r, target):

    mid = (l-r)//2+l

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return l

nums = [1,3,5,6]
k = 2
print(binary_search(nums, 0, 3, k))
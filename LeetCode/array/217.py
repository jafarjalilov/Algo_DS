# https://leetcode.com/problems/contains-duplicate/
"""
FIRST SOLUTION

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #  Time Complexity - O(n * n/2)
        #  Space Complexity - O(1)

        result = False
        for i in range(len(nums)):
           for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    result = True
                    break
        return result

"""

"""
SECOND SOLUTION

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #  Time Complexity - O(n)
        #  Space Complexity - O(n/2) - ???????

        num = 0
        result = False
        for i in range(len(nums)):
            num = nums.pop()
            if num in nums:
                result = True
        return result

"""

# USING HASHMAP
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #  Time Complexity - O(n+n)
        #  Space Complexity - O(n)

        idx_num_pairs = {}
        for index, num in enumerate(nums):
            idx_num_pairs[num] = index
        for index, num in enumerate(nums):
            if num in idx_num_pairs and idx_num_pairs[num] != index:
                return True
        return False

"""
# BETTER SOLUTION from LeetCode using set()

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #  Time Complexity - O(n)
        #  Space Complexity - O(n)
        if len(nums) == 0:
            return False
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
"""
object = Solution()
print(object.containsDuplicate([1,2,3,1]))
print(object.containsDuplicate([1,2,3,4]))
print(object.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer1 = 0
        pointer2 = 1
        while pointer2 < len(nums):
            if nums[pointer1] == nums[pointer2]:
                del nums[pointer1]
            else:
                pointer1 +=1
                pointer2 +=1 
        return len(nums)

object = Solution()

print(object.removeDuplicates([1,1,2]))
print(object.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

"""
BETTER SOLLUTION

class Solution:
    def removeDuplicates(self, nums):
        l = 1
        for r in range(1,len(nums)):
            if nums[r]!=nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l     

object = Solution()
object.removeDuplicates([1,1,2])
"""
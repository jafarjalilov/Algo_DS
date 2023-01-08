class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == val:
                nums.remove(nums[pointer])
            else: pointer += 1
        return len(nums)

object = Solution()

print(object.removeElement([3,2,2,3],3))
print(object.removeElement([0,1,2,2,3,0,4,2],2))

"""
BETTER SOLLUTION 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index_to_switch=0
        for i in range(len(nums)):
            if nums[i]==val:
                continue
            else:
                nums[index_to_switch]=nums[i]
                index_to_switch+=1
        return index_to_switch
"""
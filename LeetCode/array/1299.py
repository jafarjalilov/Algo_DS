# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        right_highest = arr[-1]
        old_element = arr[-1]

        for i in range(len(arr)-1,-1,-1):
            old_element = arr[i]
            arr[i] = right_highest

            if right_highest < old_element:
                right_highest = old_element
            
        arr[-1] = -1

        return arr

object = Solution()

print(object.replaceElements([17,18,5,4,6,1]))
print(object.replaceElements([400]))
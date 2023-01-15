# https://leetcode.com/problems/two-sum/


str1 = [3,2,4]
a = {0: 3, 1: 4, 2: 2}

def twoSum(nums, target):
    compliment = {}

    for index, num in enumerate(nums):
        compliment[target-num]=index

    for index, num in enumerate(nums):
        if num in compliment and compliment[num] != index:
            return[index, compliment[num]]

print(twoSum(str1, 6))
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        a = 1
        triangle = []

        while a <= numRows:
            row = []
            if a <= 2:
                for _ in range(a):
                    row.append(1)
                triangle.append(row)
                a += 1
                continue
            
            row.append(1)
            for i in range(a-2):
                row.append(triangle[-1][i]+triangle[-1][i+1])
            row.append(1)
            triangle.append(row)
            a += 1
        
        return triangle

object = Solution()
print(object.generate(2))
print(object.generate(3))
print(object.generate(5))

        
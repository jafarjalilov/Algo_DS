def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n-1, -1, -1):
        for j in range(n):
            reserve = []
            for k in range(n):
                reserve.append(matrix[k][j])
                matrix[k][j] = matrix[i][k]
            
            for a in range(len(reserve-1):


        
        
        









print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
# [[7,4,1],[8,5,2],[9,6,3]]
# print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
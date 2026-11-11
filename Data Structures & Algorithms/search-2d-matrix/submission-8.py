class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0])-1

        n = len(matrix[0])
        while left <= right:
            print(left, right)
            mid = (left+right)//2
            index1 = mid//n
            index2 = mid%n
            if matrix[index1][index2] == target:
                return True

            elif target > matrix[index1][index2]:
                left = mid + 1
            
            elif target < matrix[index1][index2]:
                right = mid -1 

        return False
        
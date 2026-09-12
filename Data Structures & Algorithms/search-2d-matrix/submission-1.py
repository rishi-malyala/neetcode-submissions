class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low1=0
        hi1=len(matrix)-1
        while(low1<=hi1):
            mid1 = low1 + (hi1-low1)//2

            if target == matrix[mid1][0]:
                return True
            elif target < matrix[mid1][0]:
                hi1 = mid1-1
            else:
                low1 = mid1 + 1
        
        row = hi1

        if row < 0:
            return False

        low2 = 0
        hi2 = len(matrix[0])-1
        while (low2<=hi2):
            mid2 = low2 + (hi2-low2)//2

            if target == matrix[row][mid2]:
                return True
            elif target < matrix[row][mid2]:
                hi2 = mid2-1
            else:
                low2 = mid2 + 1
        return False

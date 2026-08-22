class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return false
        
        r = len(matrix)
        c = len(matrix[0])

        left = 0
        right = (r*c)-1

        while left<=right:
            mid = (left + right) // 2

            midElem = matrix[mid//c][mid % c]

            if midElem == target:
                return True
            elif midElem < target:
                left = mid+1
            else:
                right = mid-1
        return False

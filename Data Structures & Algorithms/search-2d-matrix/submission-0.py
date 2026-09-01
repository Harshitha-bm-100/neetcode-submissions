class Solution:
    def binarySearchOn2D(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        L = 0
        R = len(matrix)-1

        while L <= R:
            MID = (L+R)//2
            if target <= matrix[MID][n-1] and target >= matrix[MID][0]:
                return MID
            if target < matrix[MID][0]:
                R = MID - 1
            elif target > matrix[MID][n-1]:
                L = MID + 1
        return -1
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        idx = self.binarySearchOn2D(matrix, target)
        if idx == -1:
            return False
        arr = matrix[idx]
        l = 0
        r = len(arr) - 1

        while l<=r:
            mid = (l+r)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
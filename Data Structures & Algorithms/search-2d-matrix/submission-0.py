class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        for x in matrix:
            array.extend(x)
        result = Solution.binarySearch(self, array, target)
        if (result != -1):
            return True
        return False
    
    def binarySearch(self, array : List[int], target: int) -> int:
        l = 0
        r = len(array) - 1
        while l <= r:
            m = (l + r) // 2
            if (array[m] == target):
                return m
            if (array[m] > target):
                r = m - 1
            else:
                l = m + 1
        return -1
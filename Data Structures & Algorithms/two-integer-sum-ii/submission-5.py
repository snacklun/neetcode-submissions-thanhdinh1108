class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,value in enumerate(numbers):
            value_find = target - numbers[i]
            val = self.binary_search(numbers,value_find)
            if (val != -1):
                return [i+1,val+1]


    def binary_search(self, number: List[int], target: int) -> int:
        low = 0
        high = len(number) - 1
        while high >= low:
            mid = low + (high - low) // 2
            if(number[mid] == target):
                return mid
            elif number[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
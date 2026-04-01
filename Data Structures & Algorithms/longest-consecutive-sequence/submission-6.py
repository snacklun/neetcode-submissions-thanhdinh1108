class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
    
        charSet = set(nums)
        result = 0
        for index, value in enumerate(charSet):
            previous_data = value - 1
            if (previous_data not in charSet):
                count = 1
                current_value = value + 1
                while current_value in charSet:
                    current_value = current_value + 1
                    count +=1
                result = max(result, count)

        return result
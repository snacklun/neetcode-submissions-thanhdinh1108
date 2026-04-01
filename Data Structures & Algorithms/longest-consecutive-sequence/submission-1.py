class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        charSet = sorted(set(nums))
        result = 0
        for index, value in enumerate(charSet):
            previous_data = value - 1
            if (previous_data not in charSet):
                count = 1
                index2 = index
                while index2 < len(charSet) - 1:
                    if(charSet[index2+1] - charSet[index2] != 1):
                        result = max(result, count)
                        break
                    else:
                        count +=1
                        index2 +=1      
                result = max(result, count)

        return result
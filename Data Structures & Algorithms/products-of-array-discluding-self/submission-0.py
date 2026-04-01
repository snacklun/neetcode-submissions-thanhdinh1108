class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i, value in enumerate(nums):
            if (i == 0):
                result.append(math.prod(nums[i+1:]))
                continue
            prefix = nums[:i]
            suffix = nums[i+1:]
            result.append(math.prod(prefix)*math.prod(suffix))
        return result
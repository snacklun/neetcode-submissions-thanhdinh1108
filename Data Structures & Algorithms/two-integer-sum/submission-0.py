class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, value in enumerate(nums):
            different = target - value
            if(different not in hash_map):
                hash_map[value] = i
            else:
                return [hash_map.get(different) , i] 
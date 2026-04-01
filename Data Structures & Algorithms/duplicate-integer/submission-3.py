class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_empty = []
        for x in nums:
            if (x not in list_empty):
                list_empty.append(x)
            else:
                return True
        
        return False
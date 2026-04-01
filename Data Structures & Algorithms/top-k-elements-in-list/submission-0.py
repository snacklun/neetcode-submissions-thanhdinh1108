class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       frequency = Counter(nums)
       return sorted(
            frequency,
            key=frequency.get,
            reverse=True
        )[:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        most_common = [num for num, _ in counts.most_common(k)]
        return most_common
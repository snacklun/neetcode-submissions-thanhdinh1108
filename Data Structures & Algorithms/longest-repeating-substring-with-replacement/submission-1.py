class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if(len(s) == 0):
            return 0

        charCounts = defaultdict(int)
        l = 0
        max_count = 0
        temp = 0
        result = 0
        for r in range(len(s)):
            if s[r] in charCounts:
                charCounts[s[r]] += 1
            else:
                charCounts[s[r]] = 1 
            max_count = max(max_count, charCounts[s[r]])
            while l <= r : 
                temp = (r - l + 1)
                if (temp - max_count <= k):
                    if(temp > result):
                        result = temp
                    break
                else:
                    charCounts[s[l]] -= 1
                    l +=1

        return result
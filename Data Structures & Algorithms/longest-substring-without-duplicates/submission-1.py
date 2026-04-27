class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
    
        l = 0
        r = 0
        result = 0
        charHash = set()
        for r in range(len(s)):
            while s[r] in charHash:
                charHash.remove(s[l])
                l += 1
            charHash.add(s[r])
            result = max(result, r  - l+1)
        return result

                

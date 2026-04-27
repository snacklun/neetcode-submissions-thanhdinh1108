class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        
        have  = defaultdict(int)
        have_count, need_count = 0, len(need)
        result_start, result_length = 0, float("inf")
        l = 0
        
        for r in range(len(s)):
            # 1. add s[r] to have
            have[s[r]] += 1
            # 2. check if have_count increases
            if(have[s[r]] == need[s[r]]):
                have_count += 1

            # 3. while valid:
            #    - record window if smaller
            #    - shrink from left
            while have_count == need_count:
                window_size = r - l + 1
                window_start = l
                if (r - l + 1) < result_length:
                    result_length = window_size
                    result_start = window_start
                    
                have[s[l]] -= 1
                if(have[s[l]] < need[s[l]]):
                    have_count -= 1
                l += 1

        
        return s[result_start: result_start + result_length] if result_length != float("inf") else ""
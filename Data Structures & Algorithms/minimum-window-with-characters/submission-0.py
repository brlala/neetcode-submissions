class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        required = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            required[c] += 1
        
        have = 0 # have tracks completed count including quantity
        need = len(required)
        res = [-1, -1]
        resLen = float("infinity")
        l = 0
        
        for r in range(len(s)):
            # add to window
            c = s[r]
            window[c] += 1

            # if matched, start shrinking
            if c in required and window[c] == required[c]:
                have += 1
            
            # record res and shart shrinking
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in required and window[s[l]] < required[s[l]]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float("infinity") else ""



        
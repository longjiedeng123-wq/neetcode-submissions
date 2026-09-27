
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_freq = [0] * 26
        for s in s1:
            i = ord(s) - ord('a')
            s1_freq[i] += 1
        cur_freq = [0] * 26

        valid_size = len(s1)
        l = 0
        for r in range(len(s2)):
            index = ord(s2[r])-ord('a')
            cur_freq[index] += 1
            
            while (r - l + 1) > valid_size:
                index = ord(s2[l])-ord('a')
                cur_freq[index] -= 1
                l += 1
            if cur_freq == s1_freq:
                return True
            
        return False
            
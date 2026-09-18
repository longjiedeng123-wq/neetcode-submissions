from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_key = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                freq[index] += 1
            
            key = tuple(freq)
            group_key[key].append(s)
            
        
        return list(group_key.values())
            

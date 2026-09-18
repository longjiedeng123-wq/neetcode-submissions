from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_key = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            group_key[key].append(s)

        return list(group_key.values())
    

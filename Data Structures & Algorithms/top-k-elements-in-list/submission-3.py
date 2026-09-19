from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in freq_count.items():
            buckets[freq].append(num)
        
        count = k
        top_k = []
        for bucket in reversed(buckets):
            if bucket:
                for num in bucket:
                    top_k.append(num)
                    count -= 1
            if count == 0:
                return top_k

        return top_k
        
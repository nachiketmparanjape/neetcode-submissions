class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        d_sorted = dict(sorted(d.items(),key=lambda x: x[1],reverse=True))
        return list(d_sorted.keys())[:k]
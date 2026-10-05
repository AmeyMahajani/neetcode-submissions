class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kv = defaultdict()

        for i in nums:
            if i in kv.keys():
                kv[i] += 1
            else:
                kv[i] = 1
        

        sorted_kv = sorted(kv, key = kv.get, reverse = True)

        return sorted_kv[:k]
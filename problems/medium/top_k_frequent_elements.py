from typing import List
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = collections.Counter(nums)
        min_heap = []
        for val, count in freq_map.items():
            heapq.heappush(min_heap, (count, val))
            while len(min_heap) > k:
                heapq.heappop(min_heap)
        return list(map(lambda tup: tup[1], min_heap))

from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elements = defaultdict(int)

        for n in nums:
            elements[n] += 1

        sorted_elements = sorted(elements, key=elements.get, reverse=True)
        return sorted_elements[:k]
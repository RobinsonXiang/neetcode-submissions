from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elements = defaultdict(int)

        for n in nums:
            elements[n] += 1

        sorted_descending = dict(sorted(elements.items(), key=lambda item: item[1], reverse=True))
        sorted_list_descending = list(sorted_descending.keys())

        result = []
        for i in range(k):
            result.append(sorted_list_descending[i])
        return result
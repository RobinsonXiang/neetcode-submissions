class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elements = defaultdict(int)

        for n in nums:
            elements[n] = 1 + elements.get(n, 0)

        count_list = [[] for _ in range(len(nums)+1)]

        for n in elements:
            count_list[elements[n]].append(n)
        
        res = []
        index = len(count_list)-1
        for i in range(len(count_list)-1, 0, -1):
           if len(count_list[i]) > 0:
            for n in count_list[i]:
                if k > 0:
                    res.append(n)
                    k = k - 1
        return res
        



            
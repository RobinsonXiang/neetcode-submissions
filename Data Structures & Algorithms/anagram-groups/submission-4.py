class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strings = {}
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in strings.keys():
                strings[sorted_word] = []

            strings[sorted_word].append(word)

        ana = []
        for sublist in strings.values():
            ana.append(sublist)

        return ana

            


    

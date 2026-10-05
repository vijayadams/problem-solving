class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        result = defaultdict(list)

        for strn in strs:
            buffer = [0] * 26
            for char in strn:
                buffer[ord(char)-ord("a")]+=1
            result[tuple(buffer)].append(strn)
        
        return list(result.values())
            
        
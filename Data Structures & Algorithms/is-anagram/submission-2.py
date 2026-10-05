"""
1. create two array with of 26 letter length
2. set the freq
3. compare both

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sfreq , tfreq = [0] * 26 , [0]*26

        for val in s:
            idx = ord(val) - ord('a')
            sfreq[idx] +=1

        for val in t:
            idx = ord(val) - ord('a') 
            tfreq[idx] +=1

        return sfreq == tfreq
        

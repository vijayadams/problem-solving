class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        required = [0] * 26
        window = [0] * 26

        # Count characters in s1
        for char in s1:
            required[ord(char) - ord('a')] += 1

        distinct = len(set(s1))
        matched = 0
        left = 0

        for right in range(len(s2)):

            # Add right character
            index = ord(s2[right]) - ord('a')
            window[index] += 1

            # Frequency became exactly correct
            if window[index] == required[index]:
                matched += 1

            # Frequency went above required
            elif window[index] == required[index] + 1:
                matched -= 1

            # Shrink window
            if right - left + 1 > len(s1):

                index = ord(s2[left]) - ord('a')

                # Removing will make it correct
                if window[index] == required[index] + 1:
                    matched += 1

                # Removing will make it incorrect
                elif window[index] == required[index]:
                    matched -= 1

                window[index] -= 1
                left += 1

            # All characters of s1 have matching frequency
            if matched == distinct:
                return True

        return False
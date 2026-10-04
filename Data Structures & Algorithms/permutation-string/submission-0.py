class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Approach:
        # 1. Count the frequency of each character in s1.
        # 2. Use a sliding window of size len(s1) in s2.
        # 3. Keep track of how many characters have the required frequency.
        # 4. When the window matches all required frequencies,
        #    it means the window is a permutation of s1.
        # 5. Move the window by adding the right character
        #    and removing the left character.

        if len(s1) > len(s2):
            return False

        # Frequency of characters required from s1
        s1_frequency = [0] * 26

        # Frequency of characters currently present in the window of s2
        s2_frequency = [0] * 26

        # Count character frequency in s1
        for char in s1:
            index = ord(char) - ord('a')
            s1_frequency[index] += 1

        # Number of distinct characters that need to match
        required_match = len(set(s1))

        # Number of characters whose frequency currently matches
        actual_match = 0

        left = 0

        for right in range(len(s2)):

            # Add the right character to the current window
            right_index = ord(s2[right]) - ord('a')
            s2_frequency[right_index] += 1

            # Frequency became exactly equal to s1's frequency
            if s2_frequency[right_index] == s1_frequency[right_index]:
                actual_match += 1

            # Frequency went above the required frequency
            elif s2_frequency[right_index] == s1_frequency[right_index] + 1:
                actual_match -= 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):

                # Character that is going to leave the window
                left_index = ord(s2[left]) - ord('a')

                # After removing this character,
                # its frequency will become exactly correct
                if s2_frequency[left_index] == s1_frequency[left_index] + 1:
                    actual_match += 1

                # Removing this character will make
                # its frequency lower than required
                elif s2_frequency[left_index] == s1_frequency[left_index]:
                    actual_match -= 1

                s2_frequency[left_index] -= 1
                left += 1

            # All required character frequencies are matching
            if actual_match == required_match:
                return True

        return False

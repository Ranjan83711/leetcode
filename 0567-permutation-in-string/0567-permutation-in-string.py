class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        for char in s1:

            if char in count1:
                count1[char] = count1[char] + 1
            else:
                count1[char] = 1

        for i in range(len(s1)):

            char = s2[i]

            if char in count2:
                count2[char] = count2[char] + 1
            else:
                count2[char] = 1

        if count1 == count2:
            return True

        for i in range(len(s1), len(s2)):

            new_char = s2[i]

            if new_char in count2:
                count2[new_char] = count2[new_char] + 1
            else:
                count2[new_char] = 1

            old_char = s2[i - len(s1)]

            count2[old_char] = count2[old_char] - 1

            if count2[old_char] == 0:
                del count2[old_char]

            if count1 == count2:
                return True

        return False
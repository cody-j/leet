'''
https://leetcode.com/problems/valid-anagram/
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counts = {}
        t_counts = {}

        for letter in s:
            if letter in s_counts:
                s_counts[letter] += 1
            else:
                s_counts[letter] = 1

        for letter in t:
            if letter in t_counts:
                t_counts[letter] += 1
            else:
                t_counts[letter] = 1

        for letter in s_counts:
            if letter not in t_counts or s_counts[letter] != t_counts[letter]:
                return False

        return True
        
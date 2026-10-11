from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        length=0
        for count in Counter(s).values():
            length+=count//2*2
        return length+(length<len(s))
        
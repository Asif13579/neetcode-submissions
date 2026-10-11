class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s=s.split()
        # length=0
        # for str in s:
        #     length=len(str)
        # return length
        return len(s.split().pop())
        
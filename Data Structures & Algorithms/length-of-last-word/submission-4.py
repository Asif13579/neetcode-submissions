class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=len(s)-1
        while (length>=0) and s[length]==' ':
            length-=1
        count=0
        while (length>=0) and s[length]!=' ':
            count+=1
            length-=1
        return count

     
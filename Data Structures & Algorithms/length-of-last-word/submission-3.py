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
        # length=i=0
        # while i<len(s):
        #     if s[i]==' ':
        #         while i<len(s) and s[i]==' ':
        #             i+=1
        #         if i==len(s):
        #             return length
        #         length=0
        #     else:
        #         length+=1
        #         i+=1
        # return length
     
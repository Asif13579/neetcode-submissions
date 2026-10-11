class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=list(words[0])
        for word in words[1:]:
            current=list(word)
            temp=[]
            for ch in common:
                if ch in current:
                    temp.append(ch)
                    current.remove(ch)
            common=temp
        return common
        
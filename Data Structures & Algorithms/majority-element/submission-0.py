class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        res=majority=0
        for num in nums:
            freq[num]=freq.get(num,0)+1
            if freq[num]>majority:
                res=num
                majority=freq[num]
        return res
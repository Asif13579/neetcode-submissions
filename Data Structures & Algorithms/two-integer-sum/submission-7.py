class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,v in enumerate(nums):
            need=target-v
            if need in dic:
                return [dic[need],i]
            dic[v]=i

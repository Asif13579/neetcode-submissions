class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        char_count={}
        for num in nums:
            char_count[num]=char_count.get(num,0)+1
        arr=[]
        for num,cnt in char_count.items():
            arr.append([cnt,num])
        arr.sort()
        res=[]
        for i in range(k):
            res.append(arr[-1-i][1])
        return res
        # char_count={}
        # for num in nums:
        #     char_count[num]=char_count.get(num,0)+1
        # arr=[]
        # for num,cnt in char_count.items():
        #     arr.append([cnt,num])
        # arr.sort()
        # res=[]
        # for i in range(k):
        #     res.append(arr[-1-i][1])
        # return res
        # char_count={}
        # for num in nums:
        #     char_count[num]=char_count.get(num,0)+1
        # arr=[]
        # for num,cnt in char_count.items():
        #     arr.append([cnt,num])
        # arr.sort()

        # res=[]
        # for i in range(k):
        #     res.append(arr[-1-i][1])
        # return res
        
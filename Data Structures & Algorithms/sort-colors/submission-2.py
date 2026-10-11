class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i,l,r=0,0,len(nums)-1
        while (l<=r):
            if nums[l]==0:
                nums[i],nums[l]=nums[l],nums[i]
                i+=1
                l+=1
            elif nums[l]==1:
                l+=1
            else:
                nums[l],nums[r]=nums[r],nums[l]
                r-=1

        # low,mid,high=0,0,len(nums)-1
        # while mid<=high:
        #     if nums[mid]==0:
        #         nums[low],nums[mid]=nums[mid],nums[low]
        #         low+=1
        #         mid+=1
        #     elif nums[mid]==1:
        #         mid+=1
        #     else:
        #         nums[mid],nums[high]=nums[high],nums[mid]
        #         high-=1
       
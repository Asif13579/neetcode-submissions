class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        copy=[num for num in nums]
        for i,num in enumerate(nums):
            nums[(i+k)%len(nums)]=copy[i]
        return nums

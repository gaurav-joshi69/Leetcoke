class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index=-1
        for i in range(0,len(nums)):
            if nums[i]==0:
                index=i
                break
        if index!=-1:
             start=index+1
             for j in range(start,len(nums)):
                if nums[j]!=0:
                    nums[j],nums[index]=nums[index],nums[j]
                    index+=1
             
        """
        Do not return anything, modify nums in-place instead.
        """
        
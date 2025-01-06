class Solution:
    def numSum(self, nums: List[int], goal: int) -> int:
        right,left,sm,count=0,0,0,0
        n=len(nums)
        while right<n:
            sm+=nums[right]
            while sm>goal and left<=right:
                sm-=nums[left]
                left+=1
            count+=right-left+1
            right+=1
        return count
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.numSum(nums,goal)-self.numSum(nums,goal-1)
        

        
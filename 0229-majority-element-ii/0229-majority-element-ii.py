class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp={}
        for num in nums:
            mp[num]=mp.get(num,0)+1
        max=len(nums)//3
        res=[]
        for num,freq in mp.items():
            if freq>max:
                res.append(num)
        return res
            
        
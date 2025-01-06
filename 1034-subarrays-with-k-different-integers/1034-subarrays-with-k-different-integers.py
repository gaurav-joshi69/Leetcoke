# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         n=len(nums)
#         left,right=0,0
#         count=0
#         mp={}
#         while right<n:
#             mp[nums[right]]=mp.get(nums[right],0)+1
#             if len(mp)>k:
#                 while len(mp)>k:
#                     mp[nums[left]]-=1
#                     if mp[nums[left]]==0:
#                         del mp[nums[left]]
#                     left+=1
#             if len(mp)==k:
#                 count+=1
#             right+=1
#         return count
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            n = len(nums)
            left, right = 0, 0
            count = 0
            mp = {}
            
            while right < n:
                mp[nums[right]] = mp.get(nums[right], 0) + 1
                
                while len(mp) > k:
                    mp[nums[left]] -= 1
                    if mp[nums[left]] == 0:
                        del mp[nums[left]]
                    left += 1
                
                count += right - left + 1
                right += 1
            
            return count
        
        return atMostK(nums, k) - atMostK(nums, k - 1)




        
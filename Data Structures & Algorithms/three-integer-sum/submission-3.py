class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        i = 0
        output = []

        while i <= len(nums)-2:
            j = len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            k = i+1
            while k < j:
                tot = nums[i]+nums[k]+nums[j]
                if tot == 0:
                    output.append([nums[i],nums[k],nums[j]])
                    k+=1
                    j-=1

                    while k<j and nums[k]==nums[k-1]:
                        k+=1
                    while k<j and nums[j]==nums[j+1]:
                        j-=1
                elif tot < 0:
                    k+=1
                else:
                    j-=1
                
            i+=1
        return output
                
                


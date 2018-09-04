class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1,0,-1):
            if nums[i] ==nums[i-1]:
                nums.remove(nums[i-1])
        print(nums)
nums = [0,0,1,1,1,2,2,3,3,4]
a=Solution()
a.removeDuplicates(nums)
        

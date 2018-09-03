class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
           for j in range(nums.index(i) + 1, len(nums)):
               if i + nums[j] == target:
                    list = [nums.index(i),j]
                    return(list)
nums = [2, 7, 11, 15]
target = 9
a = Solution()
print(a.twoSum(nums,target))

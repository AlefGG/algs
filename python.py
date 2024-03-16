class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for index in range (len(nums)):
            j = index + 1
            if (index + 1 < len(nums)):
                if nums[index] == nums[j]:
                    nums.pop(j)
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
asd = sol.removeDuplicates(nums)
print(asd)
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1
        while True:
            if (j >=  len(nums)):
                break
            if (nums[i] == nums[j]):
                nums.pop(j)
                continue
            i += 1
            j += 1
        print(nums)
        return len(nums)

nums = [1,1,2]
sol = Solution()
asd = sol.removeDuplicates(nums)
print(asd)
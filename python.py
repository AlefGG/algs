class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        nums *= 2
        return nums

nums = [1,2,3]
sol = Solution()
asd = sol.getConcatenation(nums)
print(asd)
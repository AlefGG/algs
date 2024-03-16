class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while True:
            if (i >= len(nums)):
                break
            if (nums[i] == val):
                nums.pop(i)
                continue
            i += 1
        print(nums)
        return len(nums)
          

nums = [0,1,2,2,3,0,4,2]

val = 2
sol = Solution()
asd = sol.removeElement(nums, val)
print(asd)
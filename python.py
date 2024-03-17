class Solution:
    def calPoints(self, nums: list[str]) -> int:
        stack = []
        sum = 0
        for i in range (len(nums)):
            if (nums[i] == 'D'):
                stack.append(int(stack[-1]) * 2)
            elif (nums[i] == 'C'):
                stack.remove(stack[-1])
            elif (nums[i] == '+'):
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(int(nums[i]))
        
        for i in range(len(stack)):
            sum += int(stack[i])
        return sum


ops = ["5","2","C","D","+"]
print(ops)
sol = Solution()
asd = sol.calPoints(ops)
print(asd)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        while i < len(s):
            if stack == []:
                stack.append(s[i])
                i += 1
                continue
            if stack[-1] == "{" and s[i] == "}":
                stack.pop()
            elif stack[-1] == "[" and s[i] == "]":
                stack.pop()
            elif stack[-1] == "(" and s[i] == ")":
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return stack == []


nums = "()"
sol = Solution()
asd = sol.isValid(nums)
print(asd)
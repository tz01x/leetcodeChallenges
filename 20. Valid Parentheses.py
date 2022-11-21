class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            if char in ['(','{','[']:
                stack.append(char)
            else:
                if char == ')':
                    self.pop_braked('(',stack)
                elif char == ']':
                    self.pop_braked('[',stack)
                else:
                    self.pop_braked('{',stack)
        return len(stack) == 0
    
    def pop_braked(self, char,stack):
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append('x')

sol = Solution()
print(sol.isValid("([}}])"))


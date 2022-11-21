class Solution:
    def split(self, s:str):
        item=[]
        opr = ''
        for i in range(len(s)):
            if s[i] in ['-','+','(',')',' ']:
                if opr:
                    item.append(opr)
                if s[i] != ' ':
                    item.append(s[i])
                opr = ''
            else:
                opr+=s[i]
        item.append(opr)      

        return item
    def normalize(self, s:list):
        for i in range(len(s)):
            if s[i] == '-':
                if i>0 and s[i-1] == '(':
                    s.insert(i,'0')
                elif i == 0:
                    s.insert(i,'0')
        return s 
    def calculate(self,s: str) -> int:
        s = self.split(s)
        s = self.normalize(s)
        operator_stack = []
        operant_stack = []
        
        for i in range(len(s)):
            char = s[i]
            if not char:
                continue
            if char in ['-','+','(',')']:
                if char == ')':
                    while operator_stack[-1] != '(':
                        self.do_calculation(operator_stack, operant_stack,s,i)
                    if operator_stack:
                        operator_stack.pop()
                        self.do_calculation(operator_stack, operant_stack,s,i)
                else:
                    operator_stack.append(char)
            else:
                operant_stack.append(int(char))
                self.do_calculation(operator_stack, operant_stack,s,i)
        self.do_calculation(operator_stack, operant_stack,s,i)
        return operant_stack.pop()

    def do_calculation(self, operator_stack:list, operant_stack:list,s:str,i:int):
        
            
        if len(operator_stack)>0 and operator_stack[-1] != '(':
            # if len(operator_stack)>=2 and operator_stack[-2] == '(' and operator_stack[-1] == '-' and s[i+1] == ')':
            #     # unary 
            #     b = operant_stack.pop()
            #     operator_stack.pop()
            #     operant_stack.append(-b)
        
            if len(operant_stack) >= 2:
                b = operant_stack.pop()
                a = operant_stack.pop()
                res = self.calc(a,b,operator_stack.pop())
                operant_stack.append(res)
                self.do_calculation(operator_stack,operant_stack,s,i)
            # elif len(operant_stack) == 1 and operator_stack and operator_stack[-1] == '-':
            #     b = operant_stack.pop()
            #     operator_stack.pop()
            #     operant_stack.append(-b)
        
    def calc(self, a:int,b:int,op:str):
        if op == '-':
            return a - b

        return a + b

s = Solution()
print(s.calculate("(7)-(0)+(4)"))
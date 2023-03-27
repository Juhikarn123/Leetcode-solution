class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]
        for i in s:
            if i=='(':
                stk.append(')')
            elif i=='{':
                stk.append('}')
            elif i=='[':
                stk.append(']')
            elif not stk or stk.pop()!=i:
                return False
        return not stk

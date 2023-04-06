class Solution:
    def addBinary(self, a: str, b: str) -> str:
        juhi=[]
        cy=0
        j=len(a)-1
        n=len(b)-1
        while j>=0 or n>=0 or cy:
            if j>=0:
                cy=cy+int(a[j])
                j=j-1
            if n>=0:
                cy=cy+int(b[n])
                n=n-1
            juhi.append(str(cy%2))
            cy//=2
        return''.join(juhi[::-1])

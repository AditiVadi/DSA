class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        ans=[]
        n1=len(num1)-1
        n2=len(num2)-1
        carry = 0
        ans = []

        while n1 >= 0 or n2 >= 0 or carry:
            x = n[num1[n1]] if n1 >= 0 else 0
            y = n[num2[n2]] if n2 >= 0 else 0

            total = x + y + carry
            ans.append(str(total % 10))
            carry = total // 10

            n1 -= 1
            n2 -= 1
        return "".join(ans[::-1])

            

        
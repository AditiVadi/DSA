class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=s.count(i)
        ans=[]
        for i,j in sorted(d.items(), key=lambda item: item[1]):
            ans.append(i*j)
        return "".join(ans[::-1])
        
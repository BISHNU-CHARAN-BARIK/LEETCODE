class Solution(object):
    def separateDigits(self, nums):
        ans=[]
        for i in nums:
            st=str(i)
            if len(st)==1:
                ans.append(int(st))
            else:
                for j in range(len(st)):
                    ans.append(int(st[j]))
        return ans
        
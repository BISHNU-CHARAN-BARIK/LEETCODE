class Solution(object):
    def isGood(self, nums):
        nums.sort()
        n=len(nums)
        check=[x for x in range(1,n)]
        check=check+[n-1]
        if(check==nums):
            return True
        else:
            return False
        
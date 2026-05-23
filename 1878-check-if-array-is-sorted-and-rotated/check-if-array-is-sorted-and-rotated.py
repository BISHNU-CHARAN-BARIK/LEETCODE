class Solution(object):
    def check(self, nums):
        sort_arr=sorted(nums)
        for i in range(len(nums)):
            sort_arr=sort_arr[1::]+sort_arr[0:1]
            if(sort_arr==nums):
                return True
        return False
        
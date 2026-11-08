class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output = [1]*l
        pre = [1]*l
        suf = [1]*l
        
        for i in range(1,l):
            pre[i] = pre[i-1]  * nums[i-1]
        for i in range(l-2,-1,-1):
            suf[i] = suf[i+1]*nums[i+1]
        for i in range(len(nums)):
            output[i] = pre[i]*suf[i]
        
        return output


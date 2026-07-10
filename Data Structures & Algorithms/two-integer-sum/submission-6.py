class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1
        while i < len(nums)-1:
            while j < len(nums):
                diff = target - nums[i]
                if nums[j] == diff:
                    return [i,j]
                print(nums[i])
                print(nums[j])
                print(i)
                print(j)
                j += 1
            i += 1
            j = i+1
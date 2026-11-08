class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        mult = 1
        contains_n = 0
        for n in nums:
            if n != 0:
                mult = mult * n
            else:
                contains_n += 1
        for n in nums:
            if contains_n > 1:
                output.append(0)
            elif contains_n == 1:
                if n != 0:
                    output.append(0)
                else:
                    output.append(int(mult))
            else:
                output.append(int(mult // n))
        return output

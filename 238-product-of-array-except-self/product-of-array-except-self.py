class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        answer = []

        for i in range(len(nums)):
            if i == 0:
                answer.append(1)
            else:
                prefix = prefix * nums[i-1]
                answer.append(prefix)
        
        j = len(nums) - 1

        while j >= 0:
            if j == len(nums) - 1:
                answer[j] = answer [j] * 1
            else:
                suffix = suffix * nums[j+1]
                answer[j] = suffix * answer[j]

            j -= 1

        return answer                
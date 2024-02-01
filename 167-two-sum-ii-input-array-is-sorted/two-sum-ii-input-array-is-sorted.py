class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_1, index_2 = 0, len(numbers) - 1
        result = []

        while index_1 < len(numbers):
            while index_2 > index_1:
                if numbers[index_1] + numbers[index_2] == target:
                    result.append(index_1 + 1)
                    result.append(index_2 + 1)
                    return result
                elif numbers[index_1] + numbers[index_2] > target:
                    index_2 -= 1
                else:
                    break
            index_1 += 1
        

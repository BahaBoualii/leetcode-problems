import numpy as np

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        two_dimension_array = np.array(matrix)
        one_dimension_array = two_dimension_array.ravel()

        if len(one_dimension_array) == 1:
            if one_dimension_array[0] == target:
                return True
            else:
                return False

        left, right = 0, len(one_dimension_array) - 1

        while left <= right:

            mid = (left + right) // 2

            if target > one_dimension_array[mid]:
                left = mid + 1
            elif target < one_dimension_array[mid]:
                right = mid - 1
            else:
                return True

        return False        
# Time Complexity : O(2^n), where n is the length of the candidates array.
# Space Complexity : O(m+n), where m is the target.

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        def helper(output, currSum, index):
            if currSum == target:
                result.append(list(output))
                return
            if currSum>target:
                return
            for i in range(index,len(candidates)):
                value = candidates[i]
                output.append(value)
                helper(output, currSum+value, i)
                output.pop()
    
        candidates = sorted(candidates)
        helper([], 0, 0)
        return result

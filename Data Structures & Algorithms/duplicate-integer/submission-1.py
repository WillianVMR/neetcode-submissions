class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = {}

        for num in nums:
            if num in memory:
                return True
            else:
                memory[num] = 1

        return False
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        
        for i in range(len(nums)):
            if target - nums[i] in answer:
                return [answer[target - nums[i]], i]
            else:
                answer[nums[i]] = i
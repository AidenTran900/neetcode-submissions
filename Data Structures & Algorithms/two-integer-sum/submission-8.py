class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indMap = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num

            if diff in indMap:
                return [indMap[diff], i]
            
            indMap[num] = i

        
        return [-1,-1]
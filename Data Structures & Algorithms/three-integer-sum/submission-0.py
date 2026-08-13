class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        returned = []
        for i in range(len(nums)):
            fixed = i
            left = fixed + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                tot = nums[fixed] + nums[left] + nums[right]

                if tot == 0:
                    returned.append([nums[fixed], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif tot > 0:
                    right -= 1

                else: # tot < 0
                    left += 1

        
        return returned
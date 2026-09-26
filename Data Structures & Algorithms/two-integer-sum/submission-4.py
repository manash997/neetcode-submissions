class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for val in range(len(nums)):
            real_val = nums[val]
            comp_val = target - nums[val]
            if comp_val in comp:
                inx = comp[comp_val]
                return [inx,val]
            else:
                comp[real_val] = val



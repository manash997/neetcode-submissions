class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        set_nums = set(nums)
        len_set_nums = len(set_nums)
        print(set_nums)
        if len_nums == len_set_nums:
            return False
        else:
            return True

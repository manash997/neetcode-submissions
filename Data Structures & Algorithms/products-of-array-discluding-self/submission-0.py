class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = 0
        for val in nums:
            if val == 0:
                count_zero+=1
        prod = 1
        for val in nums:
            if val != 0:
                prod *= val
        ans =[]
        for val in nums:
            if count_zero>1:
                ans.append(0)
            elif count_zero == 1:
                if val == 0:
                    ans.append(prod)
                else:
                    ans.append(0)
            else:
                temp = prod // val
                ans.append(temp)
        return ans
        
        
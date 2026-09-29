class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol = {}
        ans = []
        for val in nums:
            if val in sol:
                c = sol[val]
                c+=1
                sol[val] = c
            else:
                sol[val] = 1

        for i in range(k):
            max = 0
            max_num = 0
            for val in sol:
                c = sol[val]
                if c>max:
                    max = c
                    max_num = val
            ans.append(max_num)
            del sol[max_num]
        return ans
            


        
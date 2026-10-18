class Solution:
    def isValid(self, s: str) -> bool:
        sol = []
        mapping = {
        ')': '(',
        '}': '{',
        ']': '['
        }
        for x in s:
            if x in "({[":
                sol.append(x)
            if x in ")}]":
                if len(sol) != 0:
                    val = sol.pop()
                    if mapping[x] != val:
                        return False
                else:
                    return False
        if len(sol)==0:
            return True
        else:
            return False

        
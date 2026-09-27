class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        temp_dict = {}
        final_list = []
        for val in strs:
            sorted_val = "".join(sorted(val))
            if sorted_val in temp_dict:
                temp_dict[sorted_val].append(val)
            else:
                temp_dict[sorted_val] = [val]

        final_list = []
        for key in temp_dict:
            val = temp_dict[key]
            final_list.append(val)

        return final_list


                 
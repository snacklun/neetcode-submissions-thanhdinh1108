class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        my_dict = {index: 0 for index in range(len(strs))}
        i = 1
        for index, smaller_list in enumerate(strs):
            if (my_dict[index] != 0):
                continue
            i = i + 1
            hash_map = {}
            for char in smaller_list:
                hash_map[char] = hash_map.get(char,0) +1

            my_dict[index] = i

            for compare_list in range(index + 1, len(strs)):
                # Optimization: check length first
                if len(strs[compare_list]) != len(smaller_list):
                    continue
                    
                hash_map_compare = hash_map.copy()
                for char_value in strs[compare_list]:
                    if char_value not in hash_map_compare or hash_map_compare[char_value] == 0:
                        break
                    else:
                        hash_map_compare[char_value] -= 1
                else:
                    # FIX 4: Assign the GROUP ID to the index of the matching string
                    my_dict[compare_list] = i

            list_group_by = [strs[k] for k, v in my_dict.items() if v == i]
            
            result.append(list_group_by)
        
        return result
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        str_length = len(strs[0])
        remove_col_count = 0
        for i in range(str_length):
            prev = None
            is_valid_column = True
            for word in strs:
                if not prev:
                    prev = word[i]
                    continue
                if not (prev <= word[i]):
                    is_valid_column = False
                    break
                else:
                    prev = word[i]
            if not is_valid_column:
                remove_col_count+=1
        return remove_col_count
                

print(Solution().minDeletionSize(["a","b"]))
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map = defaultdict((int))
        for char in t:
            if char not in char_map:
                char_map[char] = 1
            else: char_map[char]+=1
        char_count = len(char_map)

        start = 0
        end = 0
        str_len = float('inf')
        out_str = ''
        while end < len(s):
            if s[end] in char_map:
                char_map[s[end]]-=1
                if char_map[s[end]] == 0:
                    char_count-=1
            end+=1

            while char_count == 0:
                if end - start < str_len:
                    str_len = end-start
                    out_str = s[start:end]

                start_char = s[start]
                if start_char in char_map:
                    char_map[start_char]+=1
                    if char_map[start_char] == 1:
                        char_count+=1

                start+=1
        return out_str

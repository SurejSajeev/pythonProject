class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        starting_index=0
        while starting_index < len(haystack)-1:
            if haystack[starting_index] != needle[0]:
                starting_index +=1
                continue
            needle_pointer = 1
            len_counter = 1
            for j in range(starting_index + 1, len(haystack)):
                if haystack[j] == needle[needle_pointer]:
                    len_counter += 1
                    needle_pointer += 1
                else:
                    len_counter = 1
                    needle_pointer = 1
                if len_counter == len(needle):
                    return starting_index
            return -1

if __name__ == '__main__':
    Solution().strStr("aaaaa", "bba")
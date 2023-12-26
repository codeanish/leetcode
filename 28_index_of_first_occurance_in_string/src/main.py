def hello():
    return ("Hello")

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)
        if needle_length > haystack_length:
            return -1
        for i in range(haystack_length - needle_length + 1):
            if haystack[i: i + needle_length] == needle:
                return i
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.strStr("sadbutsad", "sad"))
    print(sol.strStr("leetcode", "leeto"))
    print(sol.strStr("Hello", "ll"))
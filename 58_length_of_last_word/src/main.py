def hello():
    return ("Hello")


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return s.strip().split(" ")[-1]
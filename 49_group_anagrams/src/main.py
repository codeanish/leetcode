from typing import List


def hello():
    return ("Hello")

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_by_score = {}
        for s in strs:
            value = self.hash_string(s)
            if value in grouped_by_score:
                grouped_by_score[value].append(s)
            else:
                grouped_by_score[value] = [s]
        return list(grouped_by_score.values())

    def hash_string(self, s: str) -> int:
        sum = 0
        multiplier = 1
        for char in s:
            sum += ord(char)
            multiplier *= ord(char)
        return sum+multiplier
    

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    sol = Solution()
    print(sol.groupAnagrams(strs))
from typing import List


def hello():
    return ("Hello")

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)

        return result
    

if __name__ == "__main__":
    sol = Solution()
    print(sol.findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))
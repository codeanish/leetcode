def hello():
    return ("Hello")

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_map = {}
        for idx, char in enumerate(s):
            key = char_map.get(char)
            if key is None:
                char_map[char] = [idx]
            else:
                char_map[char].append(idx)
        max_result = -1
        for key in char_map:
            if len(char_map[key]) >= 2:
                result = char_map[key][-1] - char_map[key][0] - 1
                if result > max_result:
                    max_result = result
        return max_result


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLengthBetweenEqualCharacters("aa"))
    print(sol.maxLengthBetweenEqualCharacters("abca"))
    print(sol.maxLengthBetweenEqualCharacters("cbzxy"))
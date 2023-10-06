from typing import List


def hello():
    return ("Hello")

class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
        
    #     if len(s) != len(t):
    #         return False

    #     # Get array of each string as unicode code point for each character
    #     s_array = [ord(char) for char in s]
    #     t_array = [ord(char) for char in t]
        
    #     # sort the arrays
    #     s_array = self.quick_sort(s_array)
    #     t_array = self.quick_sort(t_array)

    #     # are the arrays the same?
    #     return t_array == s_array
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        return s_dict == t_dict

    def quick_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        # Takes the last value from the array and removes it from the array
        pivot_value = nums.pop()
        left_elements = []
        right_elements = []
        for num in nums:
            if num <= pivot_value:
                left_elements.append(num)
            else:
                right_elements.append(num)
        return self.quick_sort(left_elements) + [pivot_value] + self.quick_sort(right_elements)
    

if __name__ == "__main__":
    sol = Solution()
    sol.isAnagramDictionary("abc", "bcd")
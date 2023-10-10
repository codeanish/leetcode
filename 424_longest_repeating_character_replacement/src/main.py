def hello():
    return ("Hello")

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_frequency = {}
        length_of_string = len(s)
        left_index, right_index = 0, 0
        longest_substring_length = 0
        while right_index < length_of_string:
            # Move the right pointer and add the value to the character frequency map
            char = s[right_index]
            if char in character_frequency:
                character_frequency[char] += 1
            else:
                character_frequency[char] = 1

            # the 0th element is a 1 length window
            lenght_of_window = right_index - left_index + 1
            
            # If the total window length minus the most frequent character in that window is less than or equal to k, calculate the longest substring
            # otherwise move the left pointer
            if lenght_of_window - max(character_frequency.values()) <= k:
                longest_substring_length = max(longest_substring_length, lenght_of_window)
            else:
                left_char = s[left_index]
                character_frequency[left_char] -= 1
                if character_frequency[left_char] == 0:
                    character_frequency.pop(left_char)
                left_index += 1
            right_index += 1
        return longest_substring_length

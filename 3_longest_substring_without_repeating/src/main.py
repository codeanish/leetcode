def hello():
    return ("Hello")


def length_of_longest_substring(s: str) -> int:
    max_length = 0
    substring_set = set()
    # put in optimization for length if found max substring early
    for i in range(len(s)):
        max_length = max(max_length, len(substring_set))
        if len(s) - max_length < i:
            break
        substring_set = set(s[i])
        for j in range(i + 1,len(s)):
            if s[j] in substring_set:
                max_length = max(max_length, len(substring_set))
                break
            else:
                substring_set.add(s[j])
    return max(max_length,len(substring_set))


def length_of_longest_substring_window(s: str) -> int:
    length_of_string = len(s)
    if length_of_string == 0:
        return 0
    if length_of_string == 1:
        return 1
    left_index, right_index = 0,0
    unique_set = set()
    max_length = 0
    while right_index < len(s):
        if s[right_index] not in unique_set:
            unique_set.add(s[right_index])
            right_index += 1
        else:
            unique_set.remove(s[left_index])
            left_index += 1
        if len(unique_set) > max_length:
            max_length += 1
    return max_length

if __name__ == "__main__":
    # print(length_of_longest_substring('abcadefgh')) # Should be bcadefgh = 8
    print(length_of_longest_substring_window('abcad'))

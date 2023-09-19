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

# def length_of_longest_substring_right_to_left_pass(s: str) -> int:
#     max_length = 0
#     substring_set = set()
#     max_index_of_first_value = 0

#     for i in range(len(s)):
#         if len(substring_set) == 0:
#             index_of_first_value = i
#         if s[i] in substring_set:
#             for j in range(0,index_of_first_value,-1):
#                 print(j)
#             if len(substring_set) > max_length:
#                 max_length = len(substring_set)
#                 max_index_of_first_value = index_of_first_value
#             substring_set = set()
#         else:
#             substring_set.add(s[i])
#     if len(substring_set) > max_length:
#         max_length = len(substring_set)
#         max_index_of_first_value = index_of_first_value
#     for j in range(max_index_of_first_value-1,-1,-1):
#         if s[j] not in substring_set:
#             substring_set.add(s[j])
#         else:
#             break
#     # print(max_index_of_first_value)
#     return max(max_length,len(substring_set))

if __name__ == "__main__":
    print(length_of_longest_substring('abcadefgh')) # Should be bcadefgh = 8
    print(length_of_longest_substring_right_to_left_pass('abcadefgh'))
    # a b c
    # a d e f g h then add on c and b
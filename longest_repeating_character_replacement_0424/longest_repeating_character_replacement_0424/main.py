def hello():
    return ("Hello")


def character_replacement(s: str, k: int) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    right_index, left_index, max_sequence_count, sequence_count, first_change_index = 0,0,0,0,0
    changed_character = False
    first_letter = s[left_index]
    temp_k = k
    while right_index < len(s):
        if s[right_index] == first_letter:
            sequence_count += 1
            right_index += 1
        elif temp_k > 0:
            if changed_character == False:
                first_change_index = right_index
                changed_character = True
            sequence_count += 1
            right_index += 1
            temp_k -= 1
        else:
            if changed_character == True:
                left_index = first_change_index
            else:
                left_index = right_index
            changed_character = False
            temp_k = k
            right_index = left_index
            first_letter = s[left_index]
            if sequence_count > max_sequence_count:
                max_sequence_count = sequence_count
            sequence_count = 0

    return max(max_sequence_count,sequence_count)


if __name__ == "__main__":
    print(character_replacement('AAAABBAAABAA',2))

    # A A A A B B A A A B A A (replace 1)
    # Use a sliding window again here
    # increment right index whenever you have a matching character
    # If non matching character, replace with matching character up to k times
    # Stop when you hit a limit of changes and a non matching character
    # Set the left index to right index - k
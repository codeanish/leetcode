from longest_substring_without_repeating_0003 import main

def test_hello():
    assert main.hello() == "Hello"

def test_longest_substring():
    assert main.length_of_longest_substring('') == 0
    assert main.length_of_longest_substring(' ') == 1
    assert main.length_of_longest_substring('b') == 1
    assert main.length_of_longest_substring('bb') == 1
    assert main.length_of_longest_substring('aab') == 2
    assert main.length_of_longest_substring('abcabcbb') == 3
    assert main.length_of_longest_substring('bbbbb') == 1
    assert main.length_of_longest_substring('pwwkew') == 3
    assert main.length_of_longest_substring('bcadefgh') == 8

# def test_longest_substring_right_to_left():
#     assert main.length_of_longest_substring_right_to_left_pass('') == 0
#     assert main.length_of_longest_substring_right_to_left_pass(' ') == 1
#     assert main.length_of_longest_substring_right_to_left_pass('b') == 1
#     assert main.length_of_longest_substring_right_to_left_pass('bb') == 1
#     assert main.length_of_longest_substring_right_to_left_pass('aab') == 2
#     assert main.length_of_longest_substring_right_to_left_pass('abcabcbb') == 3
#     assert main.length_of_longest_substring_right_to_left_pass('bbbbb') == 1
#     assert main.length_of_longest_substring_right_to_left_pass('pwwkew') == 3
#     assert main.length_of_longest_substring_right_to_left_pass('bcadefgh') == 8


def test_longest_substring_window():
    assert main.length_of_longest_substring_window('') == 0
    assert main.length_of_longest_substring_window('a') == 1
    assert main.length_of_longest_substring_window(' ') == 1
    assert main.length_of_longest_substring_window('bb') == 1
    assert main.length_of_longest_substring_window('aab') == 2
    assert main.length_of_longest_substring_window('abcabcbb') == 3
    assert main.length_of_longest_substring_window('bbbbb') == 1
    assert main.length_of_longest_substring_window('pwwkew') == 3
    assert main.length_of_longest_substring_window('bcadefgh') == 8
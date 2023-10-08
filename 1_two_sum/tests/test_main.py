from src import main


def test_find_two_sum_in_array_example_1():
    num = [2,7,11,15]
    target = 9
    result = main.find_two_sum_in_array(num, target)
    assert 0 in result
    assert 1 in result

def test_find_two_sum_in_array_example_2():
    num = [3,2,4]
    target = 6
    result = main.find_two_sum_in_array(num, target)
    assert 1 in result
    assert 2 in result

def test_find_two_sum_in_array_example_3():
    num = [3,3]
    target = 6
    result = main.find_two_sum_in_array(num, target)
    assert 0 in result
    assert 1 in result

def test_find_two_sum_in_array_optimised_example_1():
    num = [2,7,11,15]
    target = 9
    result = main.find_two_sum_in_array_optimised(num, target)
    assert 0 in result
    assert 1 in result

def test_find_two_sum_in_array_optimised_example_2():
    num = [3,2,4]
    target = 6
    result = main.find_two_sum_in_array_optimised(num, target)
    assert 1 in result
    assert 2 in result

def test_find_two_sum_in_array_optimised_example_3():
    num = [3,3]
    target = 6
    result = main.find_two_sum_in_array_optimised(num, target)
    assert 0 in result
    assert 1 in result

def test_find_two_sum_in_array_alternative_example_1():
    num = [2,7,11,15]
    target = 9
    result = main.find_two_sum_in_array_someone_elses_solution(num, target)
    assert 0 in result
    assert 1 in result

def test_find_two_sum_in_array_alternative_example_2():
    num = [3,2,4]
    target = 6
    result = main.find_two_sum_in_array_someone_elses_solution(num, target)
    assert 1 in result
    assert 2 in result

def test_find_two_sum_in_array_alternative_example_3():
    num = [3,3]
    target = 6
    result = main.find_two_sum_in_array_someone_elses_solution(num, target)
    assert 0 in result
    assert 1 in result
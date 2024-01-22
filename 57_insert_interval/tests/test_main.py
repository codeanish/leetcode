from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_intervals_empty_intervals():
    sol = main.Solution()
    intervals = []
    new_interval = [6,11]
    result = sol.insert(intervals, new_interval)
    assert len(result) == 1
    assert result[0] == [6,11]

def test_intervals_before_first():
    sol = main.Solution()
    intervals = [[5,7],[11,14]]
    new_interval = [1,2]
    result = sol.insert(intervals, new_interval)
    assert len(result) == 3
    assert result[0] == [1,2]
    assert result[1] == [5,7]
    assert result[2] == [11,14]

def test_intervals_extend_first():
    sol = main.Solution()
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    result = sol.insert(intervals, new_interval)
    assert len(result) == 2
    assert result[0] == [1,5]
    assert result[1] == [6,9]

def test_intervals_insert_between():
    sol = main.Solution()
    intervals = [[1,2],[7,8]]
    new_interval = [4,5]
    result = sol.insert(intervals, new_interval)
    assert len(result) == 3
    assert result[0] == [1,2]
    assert result[1] == [4,5]
    assert result[2] == [7,8]

def test_intervals_multiple_overlaps():
    sol = main.Solution()
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    result = sol.insert(intervals, new_interval)
    # [[1,2], [3,10], [12,16]]
    assert len(result) == 3
    assert result[0] == [1,2]
    assert result[1] == [3,10]
    assert result[2] == [12,16]

def test_intervals_after_intervals():
    sol = main.Solution()
    intervals = [[1,2]]
    new_interval = [4,5]
    result = sol.insert(intervals, new_interval)
    assert len(result) == 2
    assert result[0] == [1,2]
    assert result[1] == [4,5]

def test_overlap_on_first():
    sol = main.Solution()
    intervals = [[2,4],[5,7],[8,10],[11,13]]
    new_interval = [3,6]
    result = sol.insert(intervals, new_interval)
    assert len(result) == 3
    assert result[0] == [2,7]
    assert result[1] == [8,10]
    assert result[2] == [11,13]
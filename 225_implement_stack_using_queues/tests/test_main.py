from src import main

def test_hello():
    assert main.hello() == "Hello"

def test_queue():
    my_queue = main.MyQueue()
    assert my_queue.is_empty() == True
    my_queue.push(1)
    my_queue.push(2)
    my_queue.push(3)
    assert my_queue.size() == 3
    assert my_queue.is_empty() == False
    assert my_queue.peek() == 1
    assert my_queue.size() == 3
    assert my_queue.pop() == 1
    assert my_queue.size() == 2
    assert my_queue.pop() == 2
    assert my_queue.size() == 1
    assert my_queue.pop() == 3
    assert my_queue.size() == 0
    assert my_queue.is_empty() == True
    assert my_queue.peek() == None
    assert my_queue.pop() == None


def test_stack():
    my_stack = main.MyStack()
    assert my_stack.empty() == True
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    assert my_stack.empty() == False
    assert my_stack.pop() == 3
    assert my_stack.top() == 2
    assert my_stack.pop() == 2
    assert my_stack.pop() == 1
    assert my_stack.empty() == True
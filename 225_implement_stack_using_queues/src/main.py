def hello():
    return ("Hello")

class MyStack:

    def __init__(self):
        self.first_queue = MyQueue()
        self.second_queue = MyQueue()

    def push(self, x: int) -> None:
        self.first_queue.push(x)

    def pop(self) -> int:
        # to remove the last in element on a stack, we need to pop all the elements from one queue and put them in the other queue
        # Then set the first queue to the second queue and re-initialize the second queue
        while not self.first_queue.is_empty():
            if self.first_queue.size() == 1:
                last_element = self.first_queue.pop()
                self.first_queue = self.second_queue
                self.second_queue = MyQueue()
                return last_element
            self.second_queue.push(self.first_queue.pop())

    def top(self) -> int:
        while not self.first_queue.is_empty():
            if self.first_queue.size() == 1:
                last_element = self.first_queue.pop()
                self.second_queue.push(last_element)
                self.first_queue = self.second_queue
                self.second_queue = MyQueue()
                return last_element
            self.second_queue.push(self.first_queue.pop())

    def empty(self) -> bool:
        return self.first_queue.is_empty()

class MyQueue:
    def __init__(self):
        self.state = []

    def push(self, x: int) -> None:
        self.state.append(x)

    def pop(self) -> int:
        if self.is_empty():
            return None
        return self.state.pop(0)

    def size(self) -> int:
        return len(self.state)

    def peek(self) -> int:
        if self.is_empty():
            return None
        return self.state[0]

    def is_empty(self) -> bool:
        if len(self.state) == 0:
            return True
        else:
            return False
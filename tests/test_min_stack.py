from problems.medium.min_stack import MinStack


def test_sample():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    min1 = min_stack.getMin()
    min_stack.pop()
    top1 = min_stack.top()
    min2 = min_stack.getMin()
    assert min1 == -3 and top1 == 0 and min2 == -2

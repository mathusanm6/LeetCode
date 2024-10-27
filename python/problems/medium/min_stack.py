class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            _, tmin = self.stack[-1]
            self.stack.append((val, min(tmin, val)))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

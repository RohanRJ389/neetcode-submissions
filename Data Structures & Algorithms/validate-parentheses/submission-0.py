class Solution:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def isValid(self, s: str) -> bool:
        matching = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in matching.values():
                self.push(char)
            elif char in matching: 
                if not self.stack or self.peek() != matching[char]:
                    return False
                self.pop()
                
        if len(self.stack) == 0:
            return True

        return False
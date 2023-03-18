class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def is_balanced(string):
    stack = Stack()
    for char in string:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            elif char == ")" and stack.peek() == "(":
                stack.pop()
            elif char == "]" and stack.peek() == "[":
                stack.pop()
            elif char == "}" and stack.peek() == "{":
                stack.pop()
            else:
                return False
    return stack.is_empty()

if __name__ == "__main__":
    string = input("Введите строку со скобками: ")
    if is_balanced(string):
        print("Сбалансированно")
    else:
        print("Несбалансированно")
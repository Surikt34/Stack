class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self.items = []

    def is_empty(self):
        """Проверка стека на пустоту. Возвращает True, если стек пуст, иначе False."""
        return len(self.items) == 0

    def push(self, item):
        """Добавляет новый элемент на вершину стека."""
        self.items.append(item)

    def pop(self):
        """Удаляет верхний элемент стека и возвращает его."""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")  # Обработка ситуации пустого стека

    def peek(self):
        """Возвращает верхний элемент стека, но не удаляет его."""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")  # Обработка ситуации пустого стека

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)


stack = Stack()
print(stack.is_empty())  # True
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())      # 3
print(stack.size())      # 3
print(stack.pop())       # 3
print(stack.size())      # 2
print(stack.is_empty())  # False
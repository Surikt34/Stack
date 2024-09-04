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

def check_balance(brackets):
    stack = Stack()
    # Словарь для хранения пар скобок
    brackets_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Проход по всем символам в строке
    for bracket in brackets:
        if bracket in brackets_pairs.values():
            # Если символ - открывающая скобка, кладем в стек
            stack.push(bracket)
        elif bracket in brackets_pairs.keys():
            # Если символ - закрывающая скобка
            if stack.is_empty() or stack.pop() != brackets_pairs[bracket]:
                return "Несбалансированно"

    # Если после всего прохождения стек пуст - значит, все скобки сбалансированы
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


print(check_balance("(((([{}]))))"))  # Сбалансированно
print(check_balance("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(check_balance("{{[()]}}"))  # Сбалансированно
print(check_balance("}{"))  # Несбалансированно
print(check_balance("{{[(])]}}"))  # Несбалансированно
print(check_balance("[[{())}]"))  # Несбалансированно
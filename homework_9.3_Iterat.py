class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start >= end:
            raise ValueError("Начальное значение должно быть меньше конечного")
        self.start = start
        self.end = end
        # Начальное значение должно быть первым чётным числом >= start
        self.current = start if start % 2 == 0 else start + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        even_number = self.current
        self.current += 2
        return even_number

# Пример использования
print('После перебора и вывода:')
en = EvenNumbers(10, 25)
for i in en:
    print(i)
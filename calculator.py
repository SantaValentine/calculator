import re


def main(expression: str) -> str:
    # Проверка ввода
    pattern = r"^(\d{1,2})\s*([^\d\s]+)\s*(\d{1,2})$"
    match = re.match(pattern, expression)
    if not match:
        raise ValueError("Некорректный формат ввода. Ожидается 'a + b', 'a - b', 'a * b' или 'a / b'.")

    # Извлечение данных
    a, operator, b = match.groups()
    a, b = int(a), int(b)

    # Проверка деления на ноль
    if operator == '/' and b == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")

    # Проверка диапазона чисел
    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")

    # Проверка допустимого оператора
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("Недопустимая операция.")

    # Выполнение операций
    result = None  # Инициализация переменной result
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a // b  # Целочисленное деление

    return str(result)


if __name__ == "__main__":
    print("Input:")
    user_input = input().strip()  # Считываем строку с выражением
    try:
        # Вычисляем результат
        output = main(user_input)
        # Печатаем вывод
        print("Output:")
        print(output)
    except Exception as e:
        print("Output:")
        print(f"Ошибка: {e}")

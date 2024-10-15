def main(input: str) -> str:
    # Разделяем входную строку по пробелам
    tokens = input.strip().split()

    # Проверяем, что есть ровно три токена: число, оператор, число
    if len(tokens) != 3:
        raise Exception("throws Exception")

    # Распаковка
    a_str, operator, b_str = tokens

    # Преобразуем в int, в случае неудачи бросаем исключение
    try:
        a = int(a_str)
        b = int(b_str)
    except ValueError:
        raise Exception("throws Exception")

    # Проверяем, что числа в диапазоне от 1 до 10 (включительно)
    if not (1 <= a <= 10) or not (1 <= b <= 10):
        raise Exception("throws Exception")

    # Выполняем операцию
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            raise Exception("throws Exception")
        result = a // b
    else:
        raise Exception("throws Exception") # Неизвестный оператор

    return str(result)


if __name__ == "__main__":
    user_input = input()
    print(main(user_input))


# ~===== Поведение как в примерах =====~ #
# if __name__ == "__main__":
#     try:
#         user_input = input()
#         print(main(user_input))
#     except Exception as e:
#         print(e)


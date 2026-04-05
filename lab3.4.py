# 3.4.py
numbers = []
for i in range(3):
    num = float(input(f"Введите число {i+1}: "))
    numbers.append(num)

average = sum(numbers) / len(numbers)
print(f"Среднее арифметическое чисел {numbers} равно {average}")

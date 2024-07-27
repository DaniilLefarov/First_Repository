array = []

for i in range(10):
    array.append(input())

sum = 0
for i in array:
    if int(i) > 100 and i[-2] == i[-1]:
        sum += int(i)

if sum:
    print(f"Сумма элементов по условию задачи: {sum}")
else:
    print("Элементов, удовлетворяющих условию задачи - НЕТ")
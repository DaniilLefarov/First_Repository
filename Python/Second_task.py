array = [[float(input()) for j in range(5)] for i in range(4)]

mul = 1
print("Двумерный массив: ")
for i in range(4):
    for j in range(5):
        print(str(array[i][j]).ljust(3), end = ' ')
        if i == j:
            mul *= array[i][j]
    print()

print()
print(f"Произведение элементов на главной диагонали: {mul}")
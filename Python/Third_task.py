my_string = input()

array_words = my_string.split()

first_word = array_words[0]
last_word = array_words[-1]

if len(first_word) == len(last_word):
    print("Длины первого и последнего слова - одинаковые")
elif len(first_word) > len(last_word):
    print("Длина первого слова больше")
else:
    print("Длина последнего слова больше")
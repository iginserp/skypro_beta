initial_list = ['hello', 'world', 'apple', 'pear', 'banana', 'pop']
result = []
for word in initial_list:
    if word[0] == word[-1]:
        result.append(word)
print(result)

list_of_numbers = [2, 3, 5, 7, 11]
list_of_numbers.sort(reverse=True)
print(list_of_numbers)
result2 = list_of_numbers[0] * list_of_numbers[1]
print("Произведение двух наибольших чисел из списка: ", result2)
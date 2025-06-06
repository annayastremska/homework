# Початковий рівень:

# task 1
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
the_sum = sum((list_of_numbers))

# task 2
the_minimum = min(list_of_numbers)

# task3
inverted_list = list_of_numbers[::-1]

# task 4
odd_numbers = []
for number in list_of_numbers:
    if number % 2 != 0:
        odd_numbers.append(number)

# task 5
new_list = []
any_number = int(input())
for number in list_of_numbers:
    new_number = number * any_number
    new_list.append(new_number)

print("Початковий рівень:")
print(f"1:{the_sum}")
print(f"2: {the_minimum}")
print(f"3: {inverted_list}")
print(f"4: {odd_numbers}")
print(f"5: {new_list}")

# Легкий рівень:

# task 1
list_without_more_than_x = []
x = int(input())
for number in list_of_numbers:
    if number < x:
        list_without_more_than_x.append(number)

# task 2
average = 0
for number in list_of_numbers:
    if number < 0:
        list_of_numbers.remove(number)
    average += sum(list_of_numbers) / len(list_of_numbers)

# task 3
max_in_filtered_list = max(list_without_more_than_x)

# task 4
Y = int(input())
list_divided_by_y = []
for number in list_of_numbers:
    if number % Y == 0:
        list_divided_by_y.append(number)
        sum_in_list_divided_by_y = sum(list_divided_by_y)

# task 5
list_of_squares = []
for number in list_of_numbers:
    list_of_squares.append(number ** 2)

# task 6
positive_list = []
for number in list_of_numbers:
    if number > 0:
        positive_list.append(number)

# task 7
list_of_words = ["перетворення", "перевірка", "сходження", "відродження"]
prefix = "пере"
list_of_new_words = []
for word in list_of_words:
    if prefix in word:
        list_of_new_words.append(word)

# task 8
N = int(input())
sum_of_N_numbers = sum(list_of_numbers[:N])

# task 9
list_of_palindromes = []
list_of_more_words = ["перетворення", "перевірка",
                      "сходження", "відродження", "Я несу гусеня", "12321"]
for word in list_of_more_words:
    if word.lower().replace(" ", "")[::-1] == word.lower().replace(" ", ""):
        list_of_palindromes.append(word)

# task 10
list_true_false = []
dilnyk = int(input())
for number in list_of_numbers:
    if number % dilnyk == 0:
        list_true_false.append(bool(number))
    else:
        list_true_false.append(not bool(number))

print("Легкий рівень:")
print(f"1: {list_without_more_than_x}")
print(f"2: {average}")
print(f"3: {max_in_filtered_list}")
print(f"4: {sum_in_list_divided_by_y}")
print(f"5: {list_of_squares}")
print(f"6: {positive_list}")
print(f"7: {list_of_new_words}")
print(f"8: {sum_of_N_numbers}")
print(f"9: {list_of_palindromes}")
print(f"10: {list_true_false}")

# Середній рівень

# task 1
list_x_y = []
X = int(input())
Y = int(input())
for number in list_of_numbers:
    if number % X == 0 and number % Y != 0:
        list_x_y.append(number)

# task 2
nested_list = [["котик", "песик"], [
    "черепашка", "крабік"], ["мишка", "їжачок"]]
full_list = []
for each_list in nested_list:
    for word in each_list:
        full_list.append(word)

# task 3
some_index = int(input())
extracted_word = (full_list.pop((some_index - 1))).capitalize()

# task 4
new_numbers = [1, 1, 1, 1, 5, 21, 21, 7, 7, 8, 3, 8, 11, 11, 11, 13]
new_numbers.sort(reverse=True)
freq_dict = {}
sorted_list = []
for number in new_numbers:
    if number in freq_dict:
        freq_dict[number] += 1
    else:
        freq_dict[number] = 1
max_freq = max(freq_dict.values())
for count in range(max_freq, 0, -1):
    for number in freq_dict:
        if freq_dict[number] == count:
            sorted_list += [number] * count

# task 5
big_list = []
unique_1 = list(set([1, 4, 3, 6, 9, 4, 0, 2]))
unique_2 = list(set([9, 5, 4, 1, 1, 0, 4, 7, 3, 8, 2]))
if len(unique_1) < len(unique_2):
    for number in unique_1:
        if number not in unique_2:
            big_list.append(number)
    for number in unique_2:
        big_list.append(number)

# task 6
fruits = [
    {"peach": 2, "banana": 4, "apple": 2},
    {"peach": 5, "banana": 2, "apple": 1},
    {"peach": 2, "banana": 5, "apple": 3}
]
aggregated = {}
for fruit_dict in fruits:
    for key, value in fruit_dict.items():
        if key in aggregated:
            aggregated[key] += value
        else:
            aggregated[key] = value

# task 7
some_numbers = [-1, -2, 0, 2, 3, 6, 9, 8, 10]
updated_list = []
for number in some_numbers:
    if number < 5:
        updated_list.append(1)
    else:
        updated_list.append(number)

# task 8
amount = 0
length = int(input())
for word in list_of_more_words:
    if len(word) > length:
        amount += 1

# task 9
list1 = ["куку", "я втомилася", "передостаннє завдання"]
list2 = ["майже все", "ура", "рятуйте"]
merged_list = []
for word1, word2 in zip(list1, list2):
    merged_words = word1 + word2
    merged_list.append(merged_words)

# task 10
again_y = int(input())
again_x = int(input())
last_list = []
for number in some_numbers:
    if number > again_x:
        multiplied_number = number * again_y
        last_list.append(multiplied_number)
    else:
        last_list.append(number)

print("Середній рівень")
print(f"1: {list_x_y}")
print(f"2: {full_list}")
print(f"3: {extracted_word}")
print(f"4: {sorted_list}")
print(f"5: {big_list}")
print(f"6: {aggregated}")
print(f"7: {updated_list}")
print(f"8: {amount}")
print(f"9: {merged_list}")
print(f"10: {last_list}")

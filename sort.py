with open('word_value.txt', 'r') as file:
    data = [line.strip().split(':') for line in file]

data_dict = {item[0]: int(item[1]) for item in data}
sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)

for item in sorted_data:
    with open('sorted_word_value.txt', 'a') as f:
        f.write(f"{item[0]}:{item[1]}\n")

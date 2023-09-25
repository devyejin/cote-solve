data_list = []

for _ in range(9):
    data_list.append(int(input()))

data_list.sort()
total_sum = sum(data_list)

found = False

for i in range(len(data_list)):
    if found:
        break

    for j in range(i + 1, len(data_list)):
        if data_list[i] + data_list[j] == total_sum - 100:
            data_list.pop(j)
            data_list.pop(i)
            found = True
            break

for data in data_list:
    print(data)

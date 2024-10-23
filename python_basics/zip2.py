mylist = [1, 2, 3]
new_list = [40, 50, 60]

for ele in map(list, zip(mylist, new_list)):
    print(ele)

list1 = [1, 2, 3, 4]
list2 = [100, 120, 30, 300]
list3 = [392, 2, 33, 1]
answer = []
for num1, num2, num3 in zip(list1, list2, list3):
    answer.append(num1+num2+num3)

print(answer)


#딕셔너리 생성하기
animals = ['cat', 'dog', 'lion']
sounds = ['meow', 'woof', 'roar']
answer = dict(zip(animals, sounds))
print(answer) # {'cat': 'meow', 'dog': 'woof', 'lion': 'roar'}
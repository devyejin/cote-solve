fruits = ['apple', 'banana', 'cherry']

for idx, fruit in enumerate(fruits, start = 1): # enumerate(fruits)를 통해서 idx랑 값 접근 가능함
    print(idx, fruit)
    
    
numbers = [10, 20, 30, 40, 50]

for i, num in enumerate(numbers):
    if num == 30:
        print(f"Found 30 at index {i}")
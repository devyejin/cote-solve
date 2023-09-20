numbers = list(map(int, input().split())) # 데이터 받고

while True:
    # idx옮겨가며 비교, 왼 > 오 자리 변경

    total_sorted = False

    for idx in range(len(numbers)-1):

        if numbers[idx] > numbers[idx+1]:
            numbers[idx], numbers[idx+1] = numbers[idx+1], numbers[idx] #크
            for num in numbers:
                print(num, end=" ")

            print()
        #numbers.sort() 는 원본을 정렬하고, 반환은 None
        #sorted() 사용해야 새로운 객체 반환
        temp_numbers = sorted(numbers)
        if numbers == temp_numbers:
            total_sorted = True

    if total_sorted:
        break

        # 다 돌았는데도 정렬이 안됐다면 다시 반복해야되는데 => while문 이용
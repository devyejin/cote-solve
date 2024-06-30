import sys

values = {
    'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 3, 'F': 3, 'G': 2, 'H': 3,
    'I': 3, 'J': 2, 'K': 2, 'L': 1, 'M': 2, 'N': 2, 'O': 1, 'P': 2,
    'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2,
    'Y': 2, 'Z': 1
}

A = list(sys.stdin.readline().rstrip())
B = list(sys.stdin.readline().rstrip())
C = []


for i in range(len(A)):
    C.append(A[i])
    C.append(B[i])

#C 값을 숫자로 변경
C = [values[char] for char in C]

#i = i + (i+1) 형태로 값을 계속 저장!

while len(C) > 2: # 값이 하나가 될 때 까지!
    new_C = []
    for i in range(len(C) - 1):
        value = ( C[i] + C[i+1] ) % 10
        new_C.append(value)
    C = new_C

print(str(C[0]) + str(C[1]))
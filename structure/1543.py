import sys

documents = sys.stdin.readline().strip()
word = sys.stdin.readline().strip()

count = 0
idx = 0

while True:
    idx = documents.find(word,idx)
    if idx == -1:
        break
    #찾는다면
    count += 1
    idx += len(word) #idx위치 이동

print(count)

#012345678
#ababababa
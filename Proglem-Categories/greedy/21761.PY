N, K = map(int, input().split())
arr = list(map(int,input().split()))
cards = []
for _ in range(N):
    card_type, card_length = input().split()
    cards.append({card_type: int(card_length)})
    
print(cards)

    
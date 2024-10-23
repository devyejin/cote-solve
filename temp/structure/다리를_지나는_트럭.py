from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights) # list O(n) -> deque O(1)
    bridge_weight = 0
    # bridge = [0] * bridge_length 
    bridge = deque([0 for _ in range(bridge_length)])  
    
    while bridge:
        arrive = bridge.popleft()
        bridge_weight -= arrive
        answer += 1
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                new = truck_weights.popleft()
                bridge_weight += new
                bridge.append(new)
            else:
                bridge.append(0)
                
    return answer
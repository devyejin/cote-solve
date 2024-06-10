def permute(nums):
    def backtrack(curr):
        print(f"backtrack called with curr: {curr}")  # 호출 트레이스 출력
        if len(curr) == len(nums):
            ans.append(curr[:])
            print(f"Complete permutation found: {curr}")  # 완성된 순열 출력
            return
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                print(f"Added {num} to curr: {curr}")  # 요소 추가 출력
                backtrack(curr)
                removed = curr.pop()
                print(f"Removed {removed} from curr: {curr}")  # 요소 제거 출력
                
    ans = []
    backtrack([])
    return ans
print(permute([1, 2]))
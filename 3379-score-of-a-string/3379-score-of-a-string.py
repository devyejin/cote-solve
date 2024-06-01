class Solution:
    def scoreOfString(self, s: str) -> int:  
        result = 0  
        asci_list = [ord(c) for c in s]
        
        for i in range(len(asci_list) - 1):
            result += abs(asci_list[i] - asci_list[i+1])
        return result




#더 효율적인 풀이법
#굳이 리스트에 담지 않고 바로 변환해서 계산
class Solution:
    def scoreOfString(self, s: str) -> int:  
        result = 0
        for i in range(len(s) - 1):
            result += abs(ord(s[i] - ord(s[i+1])))
        return result

class Solution:
    def scoreOfString(self, s: str) -> int:  
        result = 0  
        asci_list = [ord(c) for c in s]
        
        for i in range(len(asci_list) - 1):
            result += abs(asci_list[i] - asci_list[i+1])
        return result
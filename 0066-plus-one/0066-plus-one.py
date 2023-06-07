class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        total = 0
        for i in range(n-1, -1, -1):
            total += digits[i] * pow(10, n-i-1)
        
        sum1 = str(total + 1)
        res = []

        for i in range(len(sum1)-1, -1, -1):
            res.append(int(sum1[i]))

        return res[::-1]
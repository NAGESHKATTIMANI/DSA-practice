class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digit_sum = 0
        sq_digit_sum = 0

        for num in str(n):
            digit_sum += int(num)
            sq_digit_sum += int(num)**2

        if abs(sq_digit_sum - digit_sum) >= 50:
            return True
        else:
            return False

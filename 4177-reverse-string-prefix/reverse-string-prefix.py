class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        reverse_at = k
        first_half_reversed = s[:reverse_at][::-1]
        second_half = s[reverse_at:]
        print(first_half_reversed+second_half)
        return first_half_reversed+second_half     



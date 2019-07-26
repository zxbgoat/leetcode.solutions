from sys import stdin

N, K = list(map(int, stdin.readline().strip().split()))
digits = stdin.readline().strip()

digitnums = [0 for _ in range(10)]
for digit in digits:
    digitnums[digit] += 1

mostdigit = max(digitnums)
mostnum = digits[mostdigit]
print(mostdigit - )

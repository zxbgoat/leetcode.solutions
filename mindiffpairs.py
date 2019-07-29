from sys import stdin

n = int(stdin.readline().strip())
arr = sorted(list(map(int, stdin.readline().strip().split())))

sums = [arr[i]+arr[n-1-i] for i in range(n//2)]
# print(sums)
print(max(sums) - min(sums))
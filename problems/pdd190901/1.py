from sys import stdin

nums, N = stdin.readline().strip().split(';')
nums = list(map(int, nums.split(',')))
N = int(N)

odds = sorted([num for num in nums if num%2!=0])[::-1]  # 奇数
eves = sorted([num for num in nums if num%2==0])[::-1]  # 偶数
# print(odds)
# print(eves)
odnum = len(odds)
evnum = len(eves)

if evnum >= N:
    rsts = eves[:N]
else:
    rsts = eves + odds[:N-evnum]

for rst in rsts[:-1]:
    print(rst, end=',')
print(rsts[-1])

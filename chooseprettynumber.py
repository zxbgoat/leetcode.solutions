from sys import stdin
from math import fabs

N, K = list(map(int, stdin.readline().strip().split()))
digits = list(map(int, stdin.readline().strip()))
# print(digits)
nums = [0 for _ in range(10)]
for digit in digits:
    nums[digit] += 1
# print(nums)

def getcost(pvt, tgt, dgts):
    # print(pvt, tgt, dgts)
    i, cnt, cost = 1, nums[pvt], 0
    while (cnt < tgt) and (pvt+i<10 or pvt-i>=0):
        if pvt + i < 10:
            diff = min(tgt-cnt, nums[pvt+i])
            cost += i * diff
            cnt += diff
            chnum = 0
            for j in range(len(dgts)-1, -1, -1):
                if dgts[j] == pvt+i:
                    dgts[j] = pvt
                    chnum += 1
                    # print(dgts)
                if chnum >= diff:
                    break
        if cnt >= tgt:
            break
        if pvt - i >= 0:
            diff = min(tgt-cnt, nums[pvt-i])
            cost += i * diff
            cnt += diff
            chnum = 0
            for j in range(len(dgts)-1, -1, -1):
                if dgts[j] == pvt-i:
                    dgts[j] = pvt
                    chnum += 1
                    # print(dgts)
                if chnum >= diff:
                    break
        i += 1
    return cost, dgts

mincost, minchdgts = getcost(0, K, digits.copy())
# print(mincost, minchdgts)
for i in range(1, 10):
    cost, chdgts = getcost(i, K, digits.copy())
    # print(cost, chdgts)
    if cost < mincost:
        mincost = cost
        minchdgts = chdgts
print(mincost)
outdgts = ''
for dgt in minchdgts:
    outdgts += str(dgt)
print(outdgts)

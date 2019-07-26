from sys import stdin

N = int(stdin.readline().strip())
A = list(map(int, stdin.readline().strip().split()))
results = []


def plant(result, rests):
    print(result, rests)
    if sum(rests) == 0:
        results.append(result)
        return
    if len(result) >= 2 and result[-1] == result[-2]:
        return
    for i in range(N):
        if not result or (rests[i] > 0 and result[-1] != i+1):
            rests[i] -= 1
            plant(result+[i+1], rests)
            rests[i] += 1


plant([], A)
if not results:
    print('-')
else:
    for i in results[0][:-1]:
        print(i, end=' ')
    print(results[0][-1])
print(results)

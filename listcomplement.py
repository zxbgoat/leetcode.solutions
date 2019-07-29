from sys import stdin

off, n, l1, l2 = list(map(int, stdin.readline().strip().split()))
if off <= l1:
    start1 = off
    if start1 + n <= l1:
        end1 = start1 + n
        start2 = 0
        end2 = 0
    elif start1 + n <= l1 + l2:
        end1 = l1
        start2 = 0
        end2 = n - (l1 - start1)
    else:
        end1 = l1
        start2 = 0
        end2 = l2
elif off <= l1 + l2:
    start1 = l1
    end1 = l1
    start2 = off - l1
    if start2 + n <= l2:
        end2 = l2 - start2 - n + 1
    else:
        end2 = l2
else:
    start1 = l1
    end1 = l1
    start2 = l2
    end2 = l2

print(start1, end1, start2, end2)
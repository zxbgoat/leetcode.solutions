import sys

s = sys.stdin.readline().strip()
p = sys.stdin.readline().strip()


def isMatch(s: str, p: str) -> bool:
    if not p:
        return not s
    firstmatch = bool(s) and p[0] in {s[0], '.'}
    if len(p) >= 2 and p[1] == '*':
        return isMatch(s, p[2:]) or firstmatch and isMatch(s[1:], p)
    else:
        return firstmatch and isMatch(s[1:], p[1:])


print(isMatch(s, p))

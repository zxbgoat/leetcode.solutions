from sys import stdin

s = stdin.readline().strip()
p = stdin.readline().strip()


def isMatch(s, p):
    print(s, p)
    if not p:
        return not s
    if not s:
        return set(p) == set('*')
    if p[0] != '*':
        return (p[0] in {s[0], '?'}) and isMatch(s[1:], p[1:])
    else:
        return isMatch(s, p[1:]) or isMatch(s[1:], p) or isMatch(s[1:], p[1:])


print(isMatch(s, p))

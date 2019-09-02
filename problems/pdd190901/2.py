from sys import stdin

S = int(stdin.readline().strip())

tacs, tactics = [], []
def findtac(src, dst, cur, tac):
    if not len(src) and cur==dst:
        tacs.append(tac)
        return
    if not len(src):
        return
    # perform d
    findtac(src[1:], dst, cur, tac+['d'])
    findtac(src[1:], dst, src[:1]+cur, tac+['l'])
    findtac(src[1:], dst, cur+src[:1], tac+['r'])

for _ in range(S):
    src = list(stdin.readline().strip())
    dst = list(stdin.readline().strip())
    tacs = []
    findtac(src, dst, [], [])
    tactics.append(tacs)

for tacs in tactics:
    print('{')
    for tac in tacs:
        print(' '.join(tac))
    print('}')
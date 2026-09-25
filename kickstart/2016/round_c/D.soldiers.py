# https://zibada.guru/gcj/ks2016c/problems/#D

T = int(input())
for t in range(1, T+1):
    N = int(input())
    soldiers = []
    for n in range(N):
        a, d = map(int, input().split())
        soldiers += (a, d),

    def win(soldiers):
        if not soldiers:
            return False
        ma = max([x[0] for x in soldiers])
        md = max([x[1] for x in soldiers])
        if (ma, md) in soldiers:
            return True
        soldiers = list(filter(lambda x: x[0] != ma and x[1] != md, soldiers))
        return win(soldiers)
    print("Case #%d: %s" % (t, "YES" if win(soldiers) else "NO"))

# if tha max attack and defense is the same soldier
# then Alice will choose him, done.
# otherwise no one will choose the one with max attack or max defense
# since his opponent will choose the other max defense or max attack
# so we can remove the max ones from choice list and continue

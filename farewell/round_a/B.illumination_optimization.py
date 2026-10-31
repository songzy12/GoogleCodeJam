# https://codingcompetitions.withgoogle.com/codejam/round/0000000000c95b94/0000000000cad086
T = int(input())


def compute(M, R, X):
    X.append(M + R)
    count = 0

    cur_right = 0
    for i in range(len(X) - 1):
        # whether position i should be put a light
        if X[i + 1] - R <= cur_right:
            continue
        if X[i] - R > cur_right:
            return False, -1
        count += 1
        cur_right = X[i] + R

    if cur_right < M:
        return False, -1
    return True, count


for t in range(T):
    M, R, N = map(int, input().split())
    X = list(map(int, input().split()))
    possible, count = compute(M, R, X)
    if possible:
        print(f"Case #{t+1}: {count}")
    else:
        print(f"Case #{t+1}: IMPOSSIBLE")

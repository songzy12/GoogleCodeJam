# https://zibada.guru/gcj/ks2016a/problems/#A

from sys import stdin


def count_distinct_chars(name):
    return len(set(name.replace(' ', '')))


def get_sort_key(name):
    """
    First by distinct char count (descending)
    Then by lexicographical order (ascending)
    """
    return (-count_distinct_chars(name), name)


def compute_leader(names):
    names.sort(key=get_sort_key)
    return names[0]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    names = []
    for i in range(N):
        name = stdin.readline().strip()
        names.append(name)
    print(f"Case #{t}: {compute_leader(names)}")

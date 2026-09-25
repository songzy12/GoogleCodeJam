# https://zibada.guru/gcj/ks2016d/problems/#C

from collections import defaultdict

MOD = 10**9+7


def pos(c):
    return ord(c)-ord('a')


def get_key(word):
    k = [0 for i in range(26)]
    for c in word:
        k[pos(c)] += 1
    return tuple(k)


def get_ans(sen, m):
    dp = [1] + [0 for i in range(len(sen))]

    for i in range(0, len(sen)):
        # i from 0 to len(sen) - 1
        k = [0 for _ in range(26)]
        for j in range(i, -1, -1):
            # consider the substr from j to i
            k[pos(sen[j])] += 1
            if tuple(k) in m:
                dp[i+1] += dp[j] * m[tuple(k)]
                dp[i+1] %= MOD
    return dp[-1]


def get_ans_list(words, sentences):
    m = defaultdict(int)
    for word in words:
        m[get_key(word)] += 1

    ans_list = []
    for sentence in sentences:
        ans_list.append(get_ans(sentence, m))
    return ans_list


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        V, S = map(int, input().split())

        words = []
        for v in range(V):
            words.append(input())

        sentences = []
        for s in range(S):
            sentences.append(input())

        ans_list = get_ans_list(words, sentences)
        print('Case #%d: %s' % (t, ' '.join(map(str, ans_list))))

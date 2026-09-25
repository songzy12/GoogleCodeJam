# https://zibada.guru/gcj/ks2016a/problems/#D


class Card:
    def __init__(self, K, L, A, C):
        """Initializes a Card instance.
        Args:
            K (int): Maximum possible level of the card.
            L (int): Current level of the card.
            A (list of int with size K): Attack points of each level of the card.
            C (list of int with size K-1): Cost of coins from each level to the next level of this card.
        """
        self.K = K
        self.L = L
        self.A = A
        self.C = C

        self.attack_cost_pairs = self.compute_attack_cost_pairs()

    def compute_attack_cost_pairs(self):
        """Computes the attack points and cost pairs for each possible level upgrade.

        Returns:
            list of tuples: Each tuple contains (attack points, cost) for each level upgrade.
        """
        attack_cost_pairs = [(self.A[self.L - 1], 0)]
        for k in range(self.L + 1, self.K + 1):
            _, cost = attack_cost_pairs[-1]
            attack_cost_pairs.append((self.A[k - 1], cost + self.C[k - 2]))
        return attack_cost_pairs


def solve(M, cards):
    """Computes the maximum attack points with M coins and exactly 8 cards.

    Args:
        M (int): The total number of coins available.
        cards (list of Card): Each Card instance contains a list of (attack points, cost) pairs.

    Returns:
        int: The maximum attack points achievable with M coins and exactly 8 cards.
    """
    # dp[i][j][k]: the maximum attack points using only the first i cards, selecting exactly j cards, with at most k coins
    dp = [[[0 for k in range(M+1)] for j in range(9)] for i in range(N+1)]
    for i in range(1, N+1):
        card = cards[i-1]
        for j in range(1, 9):
            # Makes no sense to select j cards from the first i cards if j > i
            if j > i: 
                continue
            for k in range(M+1):
                dp[i][j][k] = dp[i - 1][j][k] # Do not select the i-th card
                for attack, cost in card.attack_cost_pairs:
                    if k >= cost:
                        # Select the i-th card with the current level upgrade
                        dp[i][j][k] = max(
                            dp[i][j][k], dp[i - 1][j - 1][k - cost] + attack)
    return dp[N][8][M]


T = int(input())
for t in range(1, T + 1):
    M, N = map(int, input().split())
    cards = []
    for n in range(N):
        K, L = map(int, input().split())
        A = list(map(int, input().split()))
        C = list(map(int, input().split()))
        cards.append(Card(K, L, A, C))

    print(f"Case #{t}: {solve(M, cards)}")

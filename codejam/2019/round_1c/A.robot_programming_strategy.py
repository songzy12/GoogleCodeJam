# 因为它可以和任一个配对，所以我们就要找到一个可以打赢任一个的策略才行。
# 对于每一个对手，我们可以找到一个获胜策略列表
# 然后查看是否有重合的获胜策略列表，或者是前缀这样子

# 每一步都和上一步是独立的
# 并且需要找到某一步其中所有的都是一样的

# 255, 500

# 好蠢啊，只要检查 500 步就可以了

T = int(input())


def solve(robots):
    res = ""
    for i in range(500):
        _set = set()
        for robot in robots:
            _set.add(robot[i % len(robot)])
        if len(_set) == 3:
            return "IMPOSSIBLE"
        elif len(_set) == 1:
            if 'P' in _set:
                res += 'S'
            elif 'S' in _set:
                res += 'R'
            else:
                res += 'P'
            return res
        else:
            if 'P' in _set and 'S' in _set:
                robots = [robot for robot in robots if robot[i % len(robot)] == 'S']
                res += 'S'
            elif 'S' in _set and 'R' in _set:
                robots = [robot for robot in robots if robot[i % len(robot)] == 'R']
                res += 'R'
            elif 'R' in _set and 'P' in _set:                
                robots = [robot for robot in robots if robot[i % len(robot)] == 'P']
                res += 'P'
    return "IMPOSSIBLE"


for t in range(1, T + 1):
    A = int(input())
    robots = []
    for _ in range(A):
        robots.append(input())
    print("Case #%d: %s" % (t, solve(robots)))
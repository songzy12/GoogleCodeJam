# 把自己的 token 放进每一个瓶子
# 但是可能会出现平局

# 前 99 个晚上往其他 19 瓶子里丢假的 token
# 比上一个胜率还要低, burden 不够强
# 23333 做题时我就是写的这个

# 模拟，放弃前 14 个瓶子，然后在前 60 个夜晚均匀地破坏
# 然后花 20 个夜晚检查每一个瓶子，然后选择最少的作为 candidate
# 然后每晚往剩余地瓶子里最少的那个加 token
# 最终把自己的放进 candidate

import sys


def _print(s):
    print(s)
    sys.stdout.flush()


T = int(input())
for t in range(1, T + 1):
    for _ in range(100):
        cur_day = int(input())
        if cur_day != 100:
            vase = (cur_day % 19) + 1
            _print("%d %d" % (vase, cur_day))
        else:
            vase = 20
            _print("%d %d" % (vase, 100))

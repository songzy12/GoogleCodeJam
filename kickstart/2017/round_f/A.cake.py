T = int(raw_input())
from collections import deque
def check(nums):
    nums_ = sorted(nums)
    nums_ = deque(nums_)
    if len(nums) % 2 == 0:
        i = (len(nums) - 1) / 2
        j = i + 1
    else:
        mid = len(nums) / 2
        if nums[mid] == nums_[0]:
            nums_.popleft()
        elif nums[mid] == nums_[-1]:
            nums_.pop()
        else:
            return False
        
        i = mid - 1
        j = mid + 1
    
    while i >= 0:
        if nums[i] == nums_[0]:
            nums_.popleft()
        elif nums[i] == nums_[-1]:
            nums_.pop()
        else:
            return False
        i -= 1
        if nums[j] == nums_[0]:
            nums_.popleft()
        elif nums[j] == nums_[-1]:
            nums_.pop()
        else:
            return False
        j += 1
    return True
    

for t in range(1, T+1):
    N = int(raw_input())
    nums = map(int, raw_input().split())
    print "Case #%d: %s" % (t, "YES" if check(nums) else "NO")

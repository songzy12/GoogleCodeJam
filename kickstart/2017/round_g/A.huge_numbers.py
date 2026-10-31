import code

T = int(raw_input())
for t in range(1, T+1):
    A, N, P = map(int, raw_input().split())

    if A % P == 0:
        print "Case #%d: %d" % (t, 0)
        continue
    
    result = {}
    product = A

    while product not in result:
        result[product] = len(result)
        product *= A
        product %= P

    # result is of size at most P

    head = result[product]
    repeat = len(result) - head

    # compute N! mod repeat

    def check():
        temp = 1
        for i in range(1, N+1):
            temp *= i
            if temp > head:
                return True
        return False

    if check():
        res = 1
        for i in range(head + repeat):
            res *= A
            res %= P

        ans = 1
        for i in range(1, N+1):
            ans = (ans * i) % repeat
        ans = (ans - (head % repeat) + repeat) % repeat

        for i in range(ans):
            res *= A
            res %= P
    else:
        temp = 1
        for i in range(1, N+1):
            temp *= i
            
        res = 1
        for i in range(temp):
            res *= A
            res %= P
        
    print "Case #%d: %d" % (t, res)
        
    
# why it is wrong: consider A = 2, P = 12
# then the result is 1, 2, 4, 8, 4, 8 ...

# also this: A = 5, P = 10
# the result is 5, 5, 5, 5
# head = 0, repeat = 1
# remember to multiply 5**repeat
# to make the answer 5, instead of 1

C0 = J0 = None

def test(C1, J1):
    global C0, J0
    if not C0:
        C0, J0 = C1, J1
    if (abs(int(C0) - int(J0)), C0, J0) > (abs(int(C1) - int(J1)), C1, J1):
        C0, J0 = C1, J1

def run(C, J, C1, J1, flag):
    if not C:
        test(C1, J1)
        return

    if flag == 1:
        run(C[1:], J[1:], C1+('0' if C[0] == '?' else C[0]),
            J1+('9' if J[0] == '?' else J[0]), 1)
        return

    if flag == -1:
        run(C[1:], J[1:], C1+('9' if C[0] == '?' else C[0]),
            J1+('0' if J[0] == '?' else J[0]), -1)
        return
    
    if C[0] != '?' and J[0] != '?':
        run(C[1:], J[1:], C1+C[0], J1+J[0],
            1 if C[0] > J[0] else -1 if C[0] < J[0] else 0)
        return

    if C[0] == J[0] == '?':
        run(C[1:], J[1:], C1+'0', J1+'0', 0)
        run(C[1:], J[1:], C1+'0', J1+'1', -1)
        run(C[1:], J[1:], C1+'1', J1+'0', 1)
        return

    if C[0] == '?':
        run(C[1:], J[1:], C1+J[0], J1+J[0], 0)
        if int(J[0]) < 9:
            run(C[1:], J[1:], C1+str(int(J[0]) + 1), J1+J[0], 1)
        if int(J[0]) > 0:
            run(C[1:], J[1:], C1+str(int(J[0]) - 1), J1+J[0], -1)
        return

    if J[0] == '?':
        run(C[1:], J[1:], C1+C[0], J1+C[0], 0)
        if int(C[0]) < 9:
            run(C[1:], J[1:], C1+C[0], J1+str(int(C[0]) + 1), -1)
        if int(C[0]) > 0:
            run(C[1:], J[1:], C1+C[0], J1+str(int(C[0]) - 1), 1)
        return
        

T = int(raw_input())
for t in range(1, T+1):
    C, J = raw_input().strip().split()
    run(C, J, '', '', 0)
    print 'Case #%d: %s %s' % (t, C0, J0)
    C0 = J0 = None
    
    

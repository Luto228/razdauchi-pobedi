import sys

sys.stdin = open('input3.txt', 'r')
sys.stdout = open('output3.txt', 'w')

while True:
    try:
        H,W,R = input().split()
        H = int(H)
        W = int(W)
        R = int(R)
        if (R*2) < W and (R*2) < H:
            print('YES')
        else:
            print('NO')
    except EOFError:
        break
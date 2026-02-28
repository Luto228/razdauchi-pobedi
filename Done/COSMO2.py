import sys

sys.stdin = open('input2.txt', 'r')
sys.stdout = open('output2.txt', 'w')

while True:
    try:
        c,h,o = input().split()
        c = int(c) // 2
        h = int(h) // 6
        o = int(o) // 1
        cho = min(c,h,o)
        print(f'{cho}')
    except EOFError:
        break
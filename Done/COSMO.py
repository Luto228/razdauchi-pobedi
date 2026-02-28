import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

while True:
    try:
        line = int(input())
        if 2 >= line > 0 or line == 12:
            print('Winter')
        elif line > 2 and line <= 5:
            print('Spring')
        elif line > 5 and line >= 6 and line < 9:
            print('Summer')
        elif line >= 9 and line <= 11:
            print('Autumn')
        else:
            print('Error')
    except EOFError:
        break
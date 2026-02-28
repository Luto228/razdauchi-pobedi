M1, M2, M3 = input().split()
M1 = int(M1)
M2 = int(M2)
M3 = int(M3)
a = False
BigMass = 0
if M1 > 727 or M1 < 94:
    print('Error')
    a = True
if M2 > 27 or M2 < 94 and a != True:
    print('Error')
    a = True
if M3 > 727 or M3 < 94 and a != True:
    print('Error')
    a = True

if M1 > M2:
    BigMass = M1
else:
    BigMass = M2
if M3 > BigMass:
    BigMass = M3

if a != True:
    print(BigMass)
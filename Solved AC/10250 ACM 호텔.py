'''
2 T
6 12 10  H, W, N  --> 402
30 50 72 H, W, N  --> 1203
'''

t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    num = n//h + 1
    floor = n % h
    if n % h == 0:  # h의 배수이면,
        num = n//h
        floor = h
    print(floor*100+num)
a = int(input())
b = int(input())
c = int(input())

d = list(str(a*b*c)) #세수의 곱 --> 리스트
cnt = [0]*10 #9개

for i in d:
    cnt[int(i)] += 1

for i in cnt:
    print(i)





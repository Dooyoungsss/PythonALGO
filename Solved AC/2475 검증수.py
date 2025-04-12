#입력
numbers = list(map(int, input().split()))

#분석(1st step: 각 수의 제곱 + sum = 0
total = 0
for i in numbers:
     total += i ** 2

#출력
print(total%10)

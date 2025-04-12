n = int(input())

#관계연산자(6개): >, >=, <, <=, ==, !=
#논리연산자(3개): and, or, not
if ((n%4 == 0) and (n%100 != 0)) or (n%400 == 0):
    print('1')
else:
    print('0')

#삼항연산식
#print('1') if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0) else print('0')
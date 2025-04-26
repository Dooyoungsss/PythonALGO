'''
목표: 사용자가 입력한 글을 비밀번호로 저장된 일기로 만듬
사용기술: file, input, if, string
추가기능: 쓴 날짜가 저장(Homework)
'''

#비밀번호 설정
PASSWORD = '1234' #추후 input으로 바꿔서 update

#사용자에게 비밀번호 입력받기
user_pw = input('👓비밀번호를 입력하세요: ')
print('Debug ------ ', user_pw)

#비밀번호가 맞는지 확인:
if user_pw == PASSWORD:
    print('👍접근 허용! 일기를 작성해 주세요.')
    diary = input('💚오늘의 일기: ')

    #파일에 저장
    with open('diary.txt', 'a', encoding='utf-8') as f:
        f.write(diary + '\n')

    print('☑️일기가 저장되었습니다.')
else:
    print('비밀번호가 틀렸습니다. 접근이 거부됩니다.')
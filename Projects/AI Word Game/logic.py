#random으로 단어를 불러오기
#오답 list 저장
#채점하기

import random
from word_data import word_dict

#오답 list를 저장하는 공간
wrong_list = []

#문제를 한개만 출제하는 함수: #Todo - 문제를 여러개 출제하게 update
def get_question(level):
    #무작위로 단어를 하나 고름
    return random.choice(word_dict[level])

#정답 확인 함수
def check_answer(correct, user_input):
    #user_input과 correct가 같은지 확인(단어를 소문자로 변환시켜준다.)
    is_correct = correct.lower() == user_input.lower()

    #비교해서 틀렸다면 wrong_list에 추가
    if not is_correct:
        wrong_list.append((correct,user_input))

    #결과를 return
    return is_correct







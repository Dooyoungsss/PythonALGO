'''
주제: 학생들이 직접 메뉴를 만들어 그중에서 점심마다 한개를 랜덤으로 추천
필요기술: random, input, list....
확장 가능: 메뉴추가/삭제, JSON 저장 , GUI 변환등으로 확장 가능
'''

import random
import json
import os


#파일 이름
JSONDB = 'menus.json'

# JSON 파일에서 메뉴 불러오기
if os.path.exists(JSONDB):
    with open(JSONDB, 'r', encoding='utf-8') as f:
        menus = json.load(f)
else:
    # 메뉴리스트 만들기
    menus = ['김밥', '떡볶이', '햄버거', '라면', '쌀국수', '치킨']

print('오늘 뭐 먹지?🍕🍔🥗🥙')
print('메뉴 목록:', menus)

#사용자가 메뉴를 입력해서 추가한다.
add = input('😊😊먹고싶은 메뉴를 하나 추가하세요 (그냥 Enter치면 추가 안됩니다.): ')
if add:
    menus.append(add)
    # 추가된 메뉴를 JSON 파일에 저장
    with open(JSONDB, 'w', encoding='utf-8') as f:
        #json.dump(data, file, ensure_ascii=True, indent=None)
        json.dump(menus, f, ensure_ascii=False, indent=2)
    print(f"'{add}'메뉴가 추가되었어요!")

#메뉴중 하나를 랜덤으로 추천
choice = random.choice(menus)
#print('Debug ---- choice value is', choice)
print(f"\n\n 오늘의 추천 메뉴는... '{choice}' 입니다!👍")


import tkinter as tk
from logic import get_question, check_answer

#게임앱을 구성하고 꾸미고 기능을 넣고
class WordGameApp:
    def __init__(self, root):
        self.level = "easy" #기본 난이도 easy

        #단어퀴즈 하나 받아오기
        self.word, self.meaning = get_question(self.level)

        #화면에 뜻을 보여주기
        self.label = tk.Label(root, text=f'뜻: {self.meaning}')
        self.label.pack() #화면에 표시

        #user가 영어단어를 입력할 입력창
        self.entry = tk.Entry(root)
        self.entry.pack()

        #결과(정답/오답)를 보여주는 label
        self.result = tk.Label(root, text='')
        self.result.pack()

        #'제출'버튼 -> 클릭하면 submit함수를 실행
        tk.Button(root, text='제출', command=self.submit).pack()
    def submit(self):
        user_input = self.entry.get() #입력값 가져오기
        #정답인지 검사
        if check_answer(self.word,user_input):
            self.result.config(text=f'✅정답!', fg='green')
        else:
            self.result.config(text=f'✖️오답! 정답은 {self.word}', fg='red')


#main.py를 실행하는 함수
def run_app():
    root = tk.Tk() #tkinter 기본창 만들기
    root.title('AI Word Game')
    WordGameApp(root) #게임제작화면 불러오기
    root.mainloop()
#tkinter : 파이썬에서 창을 만들고, 버튼, 글상자등 GUI를 구성하는 모듈
import tkinter as tk
from tkinter import messagebox #알림창을 띄우는데 사용

#To-Do 리스트를 담은 앱 클래스를 만들기
class ToDoApp:
  def __init__(self, root):
    #앱의 창 만들기
    self.root = root
    self.root.title("🔢나만의 할일 목록") #앱의 창의 제목
    self.root.geometry("400x500") #창의 크기 지정(width:400, height:500)

    #할일 데이터를 저장할 빈 리스트 만들기
    self.tasks = []

    #-------------[1] 할일 입력칸 만들기 -----------------#
    #글자를 입력할 수 있는 Entry(한줄 입력창) 만들기
    self.task_entry = tk.Entry(root, font=("Arial", 14)) #글자크기 14
    self.task_entry.pack(pady=10) #위아래 여백 10

    # -------------[2] 버튼을 담을 박스 만들기 -----------------#
    btn_frame = tk.Frame(root) #버튼들을 정렬할 수 있게 묶어주는 박스
    btn_frame.pack() #창에 올리기

    #추가버튼 만들기
    self.add_btn = tk.Button(btn_frame, text="➕추가", width=10, command=self.add_task)
    self.add_btn.grid(row=0, column=0, padx=5)

    #삭제버튼 만들기
    self.delete_btn = tk.Button(btn_frame, text="➖삭제", width=10, command=self.delete_task)
    self.delete_btn.grid(row=0, column=1, padx=5)

    # -------------[3] 할일 목록을 보여줄 리스트박스 만들기 -----------------#
    self.listbox = tk.Listbox(
        selectmode=tk.SINGLE,
        font=('Arial', 12),
        width=40,
        height=15
    )
    self.listbox.pack(pady = 10)

  #User defined 함수들
  def add_task(self):
        #입력창에 적힌 내용을 가져오기
        task = self.task_entry.get().strip() #strip()은 앞뒤 공백제거
        if task: #만약 비어있지 않다면
            self.tasks.append(task) #메모리(리스트)에 저장
            self.listbox.insert(tk.END, task) #화면의 리스트박스에도 추가
            self.task_entry.delete(0, tk.END) #입력창 초기화
        else:
            #비어있는 입력창에 추가 버튼을 눌렀을때 경고창 표시
            messagebox.showwarning("입력오류", "할 일을 먼저 입력하세요!")

  def delete_task(self):
        #선택한 항복번호 가져오기
        selected = self.listbox.curselection() #선택한 항목 번호 가져오기
        if selected: #만약 뭔가 선택되었다면
            index = selected[0]
            self.listbox.delete(index) #화면에서 삭제
            del self.tasks[index]     #리스트에서도 삭제
        else:
            #아무것도 선택안하고 삭제 버튼을 눌렀을때 경고창 표시
            messagebox.showwarning("선택오류", "삭제할 항목을 먼저 선택하세요!")

#실행코드: 프로그램 시작부분
if __name__ ==  "__main__":
  root = tk.Tk()
  root.configure(bg="lightblue")  # 창 배경색을 연파랑으로 설정
  app = ToDoApp(root)
  root.mainloop()




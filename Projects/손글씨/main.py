import tkinter as tk
from tkinter import messagebox

# 메인 앱 클래스 정의
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List")
        self.root.geometry("400x500")

        self.tasks = []  # 할 일 목록 저장

        # Entry 위젯: 사용자 입력
        self.task_entry = tk.Entry(root, font=("Arial", 14))
        self.task_entry.pack(pady=10)

        # 버튼 프레임
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.add_btn = tk.Button(btn_frame, text="➕ 추가", width=10, command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="🗑 삭제", width=10, command=self.delete_task)
        self.delete_btn.grid(row=0, column=1, padx=5)

        # 리스트박스: 할 일 목록 보여주기
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), width=40, height=15)
        self.listbox.pack(pady=10)

        # 완료 체크박스 연결용 딕셔너리 (고급 기능)
        self.done_flags = {}

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("입력 오류", "할 일을 입력하세요!")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            index = selected[0]
            self.listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showinfo("선택 오류", "삭제할 항목을 선택하세요.")

# 실행 코드
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox
import random

# --- Питання ---
QUESTIONS = [
    {"question": "Яка столиця Франції?", "options": ["Берлін", "Париж", "Мадрид"], "answer": 2},
    {"question": "Який континент найбільший за площею?", "options": ["Африка", "Азія", "Європа"], "answer": 2},
    {"question": "Який елемент має хімічний символ 'O'?", "options": ["Золото", "Кисень", "Олово"], "answer": 2},
    {"question": "Скільки хвилин у годині?", "options": ["60", "90", "45"], "answer": 1},
    {"question": "Який океан найбільший?", "options": ["Атлантичний", "Індійський", "Тихий"], "answer": 3},
    {"question": "Скільки планет у Сонячній системі?", "options": ["7", "8", "9"], "answer": 2},
    {"question": "Що є основним джерелом світла на Землі?", "options": ["Місяць", "Сонце", "Вогонь"], "answer": 2},
    {"question": "Скільки континентів на Землі?", "options": ["5", "6", "7"], "answer": 3},
    {"question": "Який газ необхідний для дихання людини?", "options": ["Кисень", "Вуглекислий газ", "Гелій"], "answer": 1},
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Quiz App")
        self.root.geometry("420x320")
        self.root.configure(bg="#e3f2fd")

        self.question_index = 0
        self.score = 0
        self.questions = random.sample(QUESTIONS, len(QUESTIONS))

        self.title_label = tk.Label(
            root, text="Mini Quiz App", font=("Arial", 16, "bold"), bg="#42a5f5", fg="white", pady=10
        )
        self.title_label.pack(fill="x")

        self.question_label = tk.Label(
            root, text="", wraplength=350, font=("Arial", 12), bg="#e3f2fd"
        )
        self.question_label.pack(pady=20)

        self.var = tk.IntVar()
        self.buttons = []
        for i in range(3):
            b = tk.Radiobutton(
                root,
                text="",
                variable=self.var,
                value=i + 1,
                font=("Arial", 11),
                bg="#e3f2fd",
                activebackground="#bbdefb",
            )
            b.pack(anchor="w", padx=60)
            self.buttons.append(b)

        self.next_button = tk.Button(
            root,
            text="Далі ▶",
            command=self.next_question,
            bg="#42a5f5",
            fg="white",
            font=("Arial", 11, "bold"),
            relief="flat",
            padx=10,
            pady=5,
        )
        self.next_button.pack(pady=20)

        self.show_question()

    def show_question(self):
        q = self.questions[self.question_index]
        self.question_label.config(text=q["question"])
        for i, option in enumerate(q["options"]):
            self.buttons[i].config(text=option)
        self.var.set(0)

    def next_question(self):
        if self.var.get() == 0:
            messagebox.showwarning("Увага", "Вибери варіант відповіді!")
            return

        correct_answer = self.questions[self.question_index]["answer"]
        if self.var.get() == correct_answer:
            self.score += 1

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.show_question()
        else:
            self.finish_quiz()

    def finish_quiz(self):
        total = len(self.questions)
        result = f"Ваш результат: {self.score}/{total}"
        if self.score >= total * 0.8:
            level = "🌟 Успішно!"
        elif self.score >= total * 0.5:
            level = "🙂 Середній рівень"
        else:
            level = "😔 Невдача"

        messagebox.showinfo("Результат", f"{result}\n{level}")
        self.root.destroy()


def run_quiz():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
    root.mainloop()

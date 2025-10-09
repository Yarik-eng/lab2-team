from typing import List, Dict, Tuple
import random
import datetime
import os

Question = Dict[str, object]

QUESTIONS: List[Question] = [
    {"question": "Яка столиця Франції?", "options": ["Берлін", "Париж", "Мадрид"], "answer": 2},
    {"question": "Який континент найбільший за площею?", "options": ["Африка", "Азія", "Європа"], "answer": 2},
    {"question": "Який елемент має хімічний символ 'O'?", "options": ["Золото", "Кисень", "Олово"], "answer": 2},
    {"question": "Скільки хвилин у годині?", "options": ["60", "90", "45"], "answer": 1},
    {"question": "Який океан найбільший?", "options": ["Атлантичний", "Індійський", "Тихий"], "answer": 3},
]

def _base_dir() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_questions(shuffle: bool = True) -> List[Question]:
    q = QUESTIONS.copy()
    if shuffle:
        random.shuffle(q)
    return q

def ask_question(q: Question) -> bool:
    print("\n" + q["question"])
    for i, opt in enumerate(q["options"], start=1):
        print(f"  {i}. {opt}")
    while True:
        choice = input("Ваш вибір (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return int(choice) == q["answer"]
        print("Некоректний ввід. Введіть 1, 2 або 3.")

def score_to_level(score: int, total: int) -> str:
    pct = score / total if total > 0 else 0
    if pct >= 0.8:
        return "Успішно"
    if pct >= 0.5:
        return "Середній рівень"
    return "Невдача"

def save_result(score: int, total: int, filepath: str = None) -> None:
    if filepath is None:
        filepath = os.path.join(_base_dir(), "data", "results.txt")
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    timestamp = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
    level = score_to_level(score, total)
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {score}/{total} | {level}\n")

def run_quiz(num_questions: int = 5, save: bool = True) -> Tuple[int, int, str]:
    questions = get_questions()
    total = min(num_questions, len(questions))
    selected = questions[:total]
    score = 0
    for q in selected:
        correct = ask_question(q)
        if correct:
            print("✅ Правильно!")
            score += 1
        else:
            print("❌ Неправильно.")
    level = score_to_level(score, total)
    print(f"\n--- Результат: {score}/{total} — {level} ---")
    if save:
        save_result(score, total)
    return score, total, level

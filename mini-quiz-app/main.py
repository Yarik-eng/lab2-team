from logic.quiz import run_quiz

def main():
    print("=== Mini Quiz App ===")
    while True:
        run_quiz(num_questions=5, save=True)
        again = input("\nСпробувати ще раз? (y/n): ").strip().lower()
        if again in ("y", "yes", "д", "так"):
            continue
        break
    print("Дякую за гру! До зустрічі.")

if __name__ == "__main__":
    main()

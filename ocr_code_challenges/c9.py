import random

def load_questions(filename):
    questions = []
    with open(filename, 'r') as f:
        for line in f:
            if line.strip():
                q, *opts, ans = line.strip().split('|')
                questions.append({
                    'question': q,
                    'options': opts,
                    'answer': ans
                })
    return questions

def generate_quiz(questions, num_questions=5):
    return random.sample(questions, min(num_questions, len(questions)))

def administer_quiz(quiz):
    user_answers = []
    for idx, q in enumerate(quiz, 1):
        print(f"Q{idx}: {q['question']}")
        for i, opt in enumerate(q['options']):
            print(f"  {chr(65+i)}. {opt}")
        ans = input("Your answer (A/B/C/D...): ").strip().upper()
        user_answers.append(ans)
    return user_answers

def grade_quiz(quiz, user_answers):
    correct = 0
    for q, ua in zip(quiz, user_answers):
        correct_ans = q['answer'].strip().upper()
        if ua == correct_ans:
            correct += 1
    print(f"\nYou scored {correct}/{len(quiz)}")

def main():
    questions = load_questions('questions.txt')
    quiz = generate_quiz(questions, num_questions=5)
    user_answers = administer_quiz(quiz)
    grade_quiz(quiz, user_answers)

if __name__ == "__main__":
    main()
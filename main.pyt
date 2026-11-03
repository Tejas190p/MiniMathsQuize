
import random

print("================================")
print("       MINI MATH QUIZ")
print("================================")

score = 0
total_questions = 5

for i in range(1, total_questions + 1):

    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)

    correct_answer = number_1 + number_2

    print(f"\nQuestion {i}:")
    user_answer = int(input(f"{number_1} + {number_2} = "))

    if user_answer == correct_answer:
        print("Correct! ")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct answer:", correct_answer)

print("\n================================")
print("          QUIZ RESULT")
print("================================")

print("Your score:", score, "/", total_questions)

if score == total_questions:
    print("Excellent! Perfect score! ")
elif score >= 3:
    print("Great job! Keep practicing! ")
else:
    print("Keep learning. You can do better! ")

print("Thanks for playing!")

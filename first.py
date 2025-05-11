score = 0

print("Welcome to the Quiz Game!")
print("You will get 1 point for each correct answer.\n")

# Question 1
print("1. What is the capital of France?")
answer = input("Your answer: ").lower()
if answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. The correct answer is Paris.\n")

# Question 2
print("2. What is 5 x 6?")
answer = input("Your answer: ")
if answer == "30":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. The correct answer is 30.\n")

# Question 3
print("3. Who wrote 'Harry Potter'?")
answer = input("Your answer: ").lower()
if "rowling" in answer or "jk rowling" in answer:
    print("Correct!\n")
    score += 1
else:
    print("Wrong. The correct answer is J.K. Rowling.\n")

# Question 4
print("4. What is the biggest planet in our solar system?")
answer = input("Your answer: ").lower()
if answer == "jupiter":
    print("Correct!\n")
    score += 1
else:
    print("Wrong. The correct answer is Jupiter.\n")

# Show Final Score
print("Quiz Finished!")
print("Your final score is:", score, "out of 4")

# Bonus message
if score == 4:
    print("Excellent job! You're a quiz master!")
elif score >= 2:
    print("Good effort!")
else:
    print("Keep learning, you'll get better!")

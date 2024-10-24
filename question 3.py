# Ask the user for a score
score = int(input("Enter a score (0-100): "))

# Categorize the score into a grade
if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score"

# Print the result
print(f"Your grade is: {grade}")

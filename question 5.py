# input
age = int(input("Enter your age: "))

# Determine if the user is a minor, adult, or senior
if age < 18:
    category = "minor"
elif 18 <= age <= 65:
    category = "adult"
else:
    category = "senior"

# Print the result
print(f"You are classified as a(n) {category}.")

print("What is type of above given Database Relational or Nonrelational?")
user_input = str(input("Enter your answer: "))

if user_input.lower() == "relational":
    print("Correct! The given database is Relational.")
elif user_input.lower() == "nonrelational":
    print("Incorrect! The given database is Relational.")
else:
    print("Invalid input! Please enter either 'Relational' or 'Nonrelational'.")

print("Thanks for answering the question!")
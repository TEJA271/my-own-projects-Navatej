password = input("Enter your password: ")

if len(password) < 8:
    print("Weak: Too short.")
elif password.isalpha() or password.isdigit():
    print("Weak: Add both letters and numbers.")
else:
    print("Strong password.")

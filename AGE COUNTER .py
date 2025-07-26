try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print("Even age")
    else:
        print("Odd age")
except:
    print("Invalid input")

import random
import string

def PasswordGenerator(length, complexity):
    if int(length) < 8:
        print("PLEASE DO NOT ENTER LENGTH LESS THAN 8")
    else:
        if complexity == "HIGH":
            print("GENERATING PASSWORD OF HIGH COMPLEXITY")
            letters = string.ascii_letters+string.digits + string.ascii_uppercase+string.punctuation+string.ascii_lowercase+string.hexdigits
            password = ''.join(random.choice(letters) for _ in range(int(length)))
            print("GENERATED PASSWORD : " + password)

        elif complexity == "MEDIUM":
            print("GENERATING PASSWORD OF MEDIUM COMPLEXITY")
            letters = string.ascii_letters + string.digits+string.punctuation
            password = ''.join(random.choice(letters) for _ in range(int(length)))
            print("GENERATED PASSWORD : " + password)

        elif complexity == "LOW":
            print("GENERATING PASSWORD OF LOW COMPLEXITY")
            letters = string.ascii_uppercase+string.punctuation
            password = ''.join(random.choice(letters) for _ in range(int(length)))
            print("GENERATED PASSWORD : " + password)

        else:
            print("WRONG COMPLEXITY ENTERED")

print("\t \t \t \n >>>>> RANDOM PASSWORD GENERATOR <<<<< \n")
length = input("ENTER LENGTH (NOT LESS THAN 8) :: ")
complexity = input("ENTER COMPLEXITY (HIGH/MEDIUM/LOW) :: ")
PasswordGenerator(length, complexity)

while True:
    choice = input("DO YOU WANT TO CONTINUE (YES/NO) :: ")
    if choice == "NO":
        break
    elif choice == "YES":
        print("\t \t \t \n >>>>> RANDOM PASSWORD GENERATOR <<<<< \n")
        length = input("ENTER LENGTH (NOT LESS THAN 8) :: ")
        complexity = input("ENTER COMPLEXITY (HIGH/MEDIUM/LOW) :: ")
        PasswordGenerator(length, complexity)
    else:
        print("INVALID INPUT")

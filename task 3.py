import random
print("PASSWORD GENERATOR!!".center(30))
char = ("qQWERTYUIOPASDFGHJKLZXCVBNMwertyuiopas#$%^&*()_+-=[]{};:,./<>?dfghjklzxcvbnm1234567890!@#$%^&*()_+-=[]{};:,./<>?")
while(True):
    lenght = int(input("Enter the lenght of the PASSWORD: "))
    password = ""
    for i in range(lenght):
        password += random.choice(char)
    print("Password:", password)
    again = input("Do you want to Generate Again! (Y/N): ").strip().lower()
    if again != "y":
        break

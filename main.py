import time
import sys

def reg(i):
    if i == "A" or i == "a":
        return "Europe"
    elif i == "B" or i == "b":
        return "Asia"
        
print("Hello! Welcome to the Capital City guessing game")

time.sleep(1)

region = input("Please select your region: \n >> A: Europe \n >> B: Asia \n")

time.sleep(1)

print("Great! Just to confirm, you have selected", reg(region))

time.sleep(1)

print("Yay! Let's play")

time.sleep(1)

score = 0

if region == "A" or region == "a":
    q1 = input("What is the capital city of England? ")
    if q1 == "London" or q1 == "london":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    q2 = input("What is the capital city of France? ")
    if q2 == "Paris" or q2 == "paris":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    
    q3 = input("What is the capital city of Italy? ")
    if q3 == "Rome" or q3 == "rome":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

elif region == "B" or region == "b":
    q1 = input("What is the capital city of Japan? ")
    if q1 == "Tokyo" or q1 == "tokyo":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

    q2 = input("What is the capital city of India? ")
    if q2 == "Dehli" or q2 == "dehli":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")
    
    q3 = input("What is the capital city of Russia? ")
    if q3 == "Moscow" or q3 == "moscow":
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

print("Thanks for playing!")

time.sleep(1)

print(f"Your final score was {score}")

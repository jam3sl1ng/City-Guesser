import time
import sys

def reg(i):
    if i == "A" or i == "a":
        return "Europe"
    elif i == "B" or i == "b":
        return "Asia"
    elif i == "C" or i == "c":
        return "North America"
    elif i == "D" or i == "d":
        return "South America"

print("Hello! Welcome to the Capital City guessing game")

time.sleep(1)

region = input("Please select your region: \n >> A: Europe \n >> B: Asia \n >> C: North America \n >> D: South America \n")

time.sleep(1)

print("Great! Just to confirm, you have selected", reg(region))

time.sleep(1)

conf = input("Is this correct? (yes / no) ")

if conf == "no" or "No":
    sys.exit()

print("Yay! Let's play")

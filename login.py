import random
import time, os, platform

#Dic

users = {
    "miguuser" : "m1gu!",

    "t3t0drill" : "t3t0r1sbr3ad",

    "ak1t4y3llow" : "sT0pN4ggInME!",
}

number_of_attempts = 3
attempts = 0
print("Welcome...")
time.sleep(2)
os.system('clear')

while True: 
    Username = input("Insert your Username: ").strip().lower() 
    attempts += 1

    if Username in users:
        print("Veryfing...")
        time.sleep(3)
        print("User found correctly...")
        break 

    else:
        print("Veryfing...")
        time.sleep(3)
        print("User not found...")
    

    if attempts >= number_of_attempts:

        print("Number of attempts exceeded")

        print("Closing Program...")
        time.sleep(2)
        exit()


#number limit of the attempts
z = 3
#number of the attempts
x = 0


while True:
    x = x+1
    passwd = (input("Password: "))

    if passwd in users[Username]:
        print("Veryfing...")

        time.sleep(2)
        os.system('clear') 
        print("Welcome! ", Username)
        time.sleep(1.5)
        try:
            import questions
            os.system('clear')
        except ModuleNotFoundError: #if module not found
            print("!ERROR!")
            time.sleep(1)
            print("Module questions.py not found, verify the name or the directory if exists... Closing program...")
            time.sleep(1) 
            exit()

        print("Checking latest system...")
        time.sleep(3)

        print(platform.system(), "|| platform info: ", platform.platform(), "|| ")

        print("Checking the network name of the computer...")
        time.sleep(3)
        print("Network name of the computer: ", platform.node())

        print("Detecting architecture...")
        time.sleep(2)
        print("Architecture of python ejecutable: ", platform.machine())

        print("Loading Program...")
        time.sleep(5)

        print("Can you wait some seconds... maybe? so, take a coffee while :)")
        time.sleep(10)
        break

    else:

        print("Incorrect Password...")

    if x >= z:

        print("To many attempts")

        print("Closing program...")
        time.sleep(2.5)
        exit()

print("You want to open extra software? just only for demostrationt purposes :)")
another_mesagge = input("R:")

if another_mesagge == "yes":
    import fpl
else:
    print("have a nice day :D")
    exit()

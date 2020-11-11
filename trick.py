# name of the customer

name = input("What is your name :  ")
print("Let's play the Math trick Game")
while True:

    gues_num = int(input("Guess the number >> "))
    print("Multiply guessed number by 2,")
    gues_num2 = gues_num * 2

    ip1 = str(input("if you are done then type Yes to continue... >> ").upper())
    if ip1 != "YES":
        print("Sorry !! I don't understand that")
        break
    else:
        print("*"*100)
        print("Now add a random number to your answer ")

    ip2 = str(input("if you are done then type Yes to continue... >>").upper())
    rnd_num = int(input("Enter that Random number >> "))
    final = rnd_num + gues_num2


    if ip2 != "YES":
        print("Sorry !! I don't understand that")
        break
    else:
        print("*" * 100)
        print("Now divide the result by 2 ")
    final = final / 2
    ip3 = str(input("if you are done then type Yes to continue... >>").upper())
    if ip3 != "YES":
        print("Sorry !! I don't understand that")
        break
    else:
        print("*" * 100)
        print("Now, Subtract guessed number from the result ")
    final = final - gues_num

    ip4 = str(input("if you are done then type Yes to continue... >>").upper())
    if ip4 != "YES":
        print("Sorry !! I don't understand that")
        break
    else:
        print("*" * 100)
        print(f"Your final answer is {final}")
        break
print(f"Thanks for playing Ms/Mrs {name}")
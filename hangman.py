
while True:
    word="hello"
    guess= input("Enter a guess \n")
    # print(guess)

    for i in word:
        if guess == i:
            print(guess,end=" ")
        else:
            print("_",end=" ")

# Store guesses [],()
# Make sure in your in for loop that you print previous guesses
# Lives=5, if guess is wrong then life -- else you will print as before
# Lives=0, Break and print("Game Over/Suicide")


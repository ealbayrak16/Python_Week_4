import random, time
def game ():
    print("Welcome to Number Guessing Game. Guess Numbers From Between 0-100")
    computer_number= random.randrange(1,101)
    start_time = time.time()
    count = 0
    while True:
        count += 1
        guess= int(input("Please Enter Your Guess : "))
        if guess<0 or 100<guess:
            print("Your Guess Number Must Be Between 0-100")
        elif computer_number == guess:
            end_time = time.time()
            print(f"Congratulations...You Guessed Correctly İn {count} Times and {int(end_time-start_time)} Seconds Time ")
            break
        elif abs(computer_number-guess)<10:
            if computer_number>guess:
                print("You approached.Guess Up A Little")
            else:
                print("You approached.Guess Down A Little")
        else:
            if computer_number>guess:
                print("Your Guess İs Too Low")
            else:
                print("Your Guess İs Too High")
game()
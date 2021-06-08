def guess_number():
    print("Think of number in range 0-1000")
    min_input = 0
    max_input = 1000
    user_answer = ""
    while user_answer != "You won":
        guess = int((max_input - min_input) / 2) + min_input
        print(f"Is your number: {guess}")
        user_input_2 = input("Enter your answer (too big, too small, you won): ")
        user_answer = user_input_2
        if user_input_2 == "too big":
            max_input = guess
        elif user_input_2 == "too small":
            min_input = guess
        elif user_input_2 == "you won":
            print("I won !")
            break
        else:
            user_input_2 = input("Wrong answer, try again. n/Enter your answer (too big, too small, you won)")


if __name__ == '__main__':
    guess_number()

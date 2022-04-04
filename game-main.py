from Functions import newgame

def newgame():
    guesses= []
    right_gueses = 0
    counter=1
    for key in questions:
        print("--------------------")
        print(key)
        for i in answers[counter-1]:
            print(i)
        guess = input("Enter (A,B,C OR D): ")
        while guess not in ("A","B","C","D"):
            guess= input("Enter (A,B,C OR D): ")
            guess=+1

        guesses.append(guess)

        right_gueses += check_answer(questions.get(key),guess)
        if counter ==10 and check_answer(questions.get(key),guess) ==1:
            right_gueses +=1

        if counter % 3 == 0:
            print("Your Mid score is:", round(right_gueses*(100/9),2))
        counter +=1

    score(right_gueses,guesses)


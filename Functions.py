from questionsDictionary_answersList import questions, answers

name= input("Enter your name:")
print("Hello",name,",this is capital cities trivia game!!! ")
print("Have fun :-)")
print()

#פונקציה שקוראת למשחק (רשימת ניחושים, תשובות נכונות, סופר שאלות ומדפיסה )

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

        guesses.append(guess)

        right_gueses += check_answer(questions.get(key),guess)
        if counter ==10 and check_answer(questions.get(key),guess) ==1:
            right_gueses+=1
        if counter % 3 == 0:
            print("Your Mid score is:", round(right_gueses*(100/9),2))
        counter +=1

    score(right_gueses,guesses)

# פונקציה שמשווה בין הניחוש לתשובה הנכונה ומחזירה ניקוד
def check_answer(answer,guess):

    if answer == guess:
        print("Correct answer")
        return 1
    else:
        print("Wrong answer")
        return 0


#פונקציה לחישוב הנקודות -ניחושים לעומת התשובות הנכונות ומחזירה את התשובות הנכונות+
# את הניחושים של השחקן+ מחשבת ניקוד

def score(right_guesses,guesses):
    print("--------------------")
    print("Results")
    print("--------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score1=int((right_guesses*(100/9)))

    print("Your score is : " + str(score1) +" "+ "POINTS")
    print()
    print("G   A  M  E       O   V  E   R ! !")


newgame()




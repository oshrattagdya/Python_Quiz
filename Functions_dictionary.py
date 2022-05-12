def newgame():
    guesses= []
    right_gueses = 0
    questions_num=1
    count = 0
    for key in questions:
        print("--------------------")
        print(key)
        count+=1
        if count==3:
            print("THIS IS THE TOTAL SCORE")
        for i in answers[questions_num-1]:

            print(i)
        guess = input("Enter (A,B,C OR D): ")
        guess = guess.upper()
        guesses.append(guess)

        right_gueses += check_answer(questions.get(key),guess)
        questions_num +=1

    score(right_gueses,guesses)


def check_answer(answer,guess):
    if answer == guess:
        print("Correct answer")
        return 1
    elif answer[-1]==guess:
        return 20
    else:
        print("Wrong answer")
        return 0


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

    score1=int((right_guesses*10))
    print("Your score is : " + str(score1) +" "+ "POINTS")

def newroud():
    pass


questions = {
"ROUND 1: \n1. In which country would you find the capital city of Sofia? : ": "A",
"2. What is the capital city of Italy?  :": "B",
"3. What 4 capital cities does the Danube river run through? : ": "A",
"ROUND 2: \n4. What is the capital city of Poland?:": "B",
"5. What capital city would you be in if you were on a boat on the Seine river? :": "A",
"6. What is the capital city of Spain?:": "C",
"ROUND 3: \n7. In what capital city would you find the Acropolis?:": "A",
"8. What is the capital city of Germany?": "C",
"9. What is the capital city of Switzerland? ": "A",
"BONUS QUESTION: \n10. What green vegetable shares its name with a European capital city?": "B"
}


answers=[["A.Bulgaria ","B.Italy ","C.France ","D.Spain  "],
         ["A.Paris ","B.Rome ","C.Vinna ","D.Madrid" ],
         ["A. Vienna,Budapest,Bratislava,Belgrade", "B.Rome, Paris,Tel-aviv,barcelona", "C.Sofia, Budapest", "D.Kyiev,Mosccow"],
         ["A.Paris","B. Warsaw", "C.NYC" , "D.Amsterdam"],
         ["A.Paris" , "B. Barcelona" ,"C.Varna" ,"D.Madrid"],
         ["A.Istanbul", "B. Warsaw", "C.Madrid", "D.Amsterdam"],
         ["A.Athens", "B. Prague" , "C.Tbilisi" , "D.Baku"],
         ["A.London", "B. Ankara", "C.Berlin", "D.Stockholm"],
         ["A.Bern", "B. Warsaw", "C.Riga", "D.Oslo"],
         ["A.Dublin", "B. Brussels", "C.Minsk", "D.Tirana"]]

newgame()




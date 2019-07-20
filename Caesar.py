def ceasar():
    alpha=input("Please enter a word or sentence to decrypt: ")
    n=4
    bet='abcdefghijklmnopqrstuvwxyz'
    s=""
    if len(alpha)<1:
        print("You did not enter anything")
    for i in range(len(alpha)):
        if  alpha[i] not in bet and alpha[i] != " ":
            print("Invalid input!!! Enter only words consisting of only letters")
            s=""
            break
        else:
            if alpha[i] == " ":
                s+=" "
            elif (n+bet.index(alpha[i].lower()))<26:
                if alpha[i].islower():
                    s+=bet[bet.index(alpha[i])+n].lower()
                else:
                    s+=bet[bet.index(alpha[i].lower())+n].upper()
            else:
                if alpha[i].islower():
                    s+=bet[bet.index(alpha[i])+n-26].lower()
                else:
                    s+=bet[bet.index(alpha[i].lower())+n-26].upper()
    print(s)
    ans=input("Do you want to try this again? y or n")
    if ans.lower().startswith('y'):
        ceasar()
    else:
        print("Thank you for using the ceasar encryption algorithm")

ceasar()


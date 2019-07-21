def caesar():
    alpha=input("Please enter a word or sentence to encrypt: ")
    n=4 #A default letter shift of 4
    bet='abcdefghijklmnopqrstuvwxyz'
    s=""
    if len(alpha)<1:
        print("You did not enter anything")
    for i in range(len(alpha)):
        if  alpha[i].lower() not in bet and alpha[i] != " ":
            s=""
            s+="Invalid input!!! Enter words consisting of only letters"
            break
        else:
            if alpha[i] == " ":
                s+=" "
            elif (n+bet.index(alpha[i].lower()))<26: #if index is within range of the string bet "
                if alpha[i].islower():
                    s+=bet[bet.index(alpha[i])+n].lower()
                else:
                    s+=bet[bet.index(alpha[i].lower())+n].upper()
            else:      #if index is outside the range of the string bet "
                if alpha[i].islower():
                    s+=bet[bet.index(alpha[i])+n-26].lower()
                else:
                    s+=bet[bet.index(alpha[i].lower())+n-26].upper()
    print(s)
    ans=input("Do you want to try this again? y or n: ")
    if ans.lower().startswith('y'):
        caesar()
    else:
        print("Thanks for using the Caesar encryption algorithm.")

caesar()


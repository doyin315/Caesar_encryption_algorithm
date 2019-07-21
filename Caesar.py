def caesar():
    alpha=input("Please enter a word or sentence to encrypt: ")
    n=4 #A default letter shift of 4
    bet='abcdefghijklmnopqrstuvwxyz'
    s="Result: "
    if len(alpha)<1:        #accounting for if the user enters nothing at all
        print("You did not enter anything")
    for i in range(len(alpha)):
        if  alpha[i].lower() not in bet and alpha[i] != " ":     #accounting for if the user enters a number or special character
            s=""
            s+="Invalid input!!! Enter words consisting of only letters"
            break
        else:
            if alpha[i] == " ":      #accounting for space entries
                s+=" "
            elif (n+bet.index(alpha[i].lower()))<len(bet):       #if index is within range of the string bet "
                if alpha[i].islower():
                    s+=bet[bet.index(alpha[i])+n]
                else:
                    s+=bet[bet.index(alpha[i].lower())+n].upper()
            else:              #if index is outside the range of the string bet "
                if alpha[i].islower():
                    s+=bet[bet.index(alpha[i])+n-len(bet)]
                else:
                    s+=bet[bet.index(alpha[i].lower())+n-len(bet)].upper()
    print(s)
    ans=input("Do you want to try this again? y or n: ")        #prompting user to try again
    if ans.lower().startswith('y'):
        caesar()             #function calls itself if user wishes to try again
    else:
        print("Thanks for using the Caesar encryption.")

caesar()


def permutation(): #order is relevant, ex. AB and BA are different
    userList = inputList() #user's list of terms
    permList = [] #final list of permutations that's being returned
    adder = findConcatenatingTerm(userList) # " + "  " & " etc
    for term in userList:
        tempCombo = term + adder
        count = 0
        while count < len(userList):
            if userList[count] != term:
                tempCombo += userList[count]
                permList.append(tempCombo)
                tempCombo = term + adder
            count += 1
    return permList

def findConcatenatingTerm(listWithStrings): #good enough
    plusCount = 0
    amperCount = 0
    for term in listWithStrings:
        for character in term:
            if character == "+":
                plusCount += 1
            if character == "&":
                amperCount += 1
    if (plusCount == 0) and (amperCount != 0):
        concatenatingTerm = " + "
    elif (plusCount != 0) and (amperCount == 0):
        concatenatingTerm = " & "
    elif (plusCount == amperCount) and (plusCount == 0):
        concatenatingTerm = " " + idiotProof("What would you like to use to put the terms together?", ["&", "+"]) + " "
    else: concatenatingTerm = " and " #neither are 0

    return concatenatingTerm

def idiotProof(question, acceptedValuesList):
    userInput = None
    while userInput not in acceptedValuesList:
        print(question)
        print("Please type one of the following values:")
        print(acceptedValuesList)
        userInput = (input("> ")).lower()
    return userInput

def inputList(): #doesn't need idiotProof bc no specific accepted values
    userList = []

    userInput = input("What's the first item in the list?\n> ")

    print("What's the next item in the list?\nType 'done' when the list is complete.")
    while userInput.lower() != "done":
        userList.append(userInput)
        userInput = input("> ")

    return userList


print("""Permutation Calculator!\n
  Type any amount of terms below and view all possible pair combinations.
  Remember, these are permutations, so order matters! For example, if your terms are 'A' and 'B', 'AB' and 'BA' will be shown as two separate permutations.
  Let's begin!\n""")

perm = permutation()
print("\n\n\nHere's your final list! Each pair is separated by a comma.\n")
print(perm)


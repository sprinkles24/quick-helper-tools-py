#DOES THIS WORK?
#DOES IT???
termList = ["a", "b", "c"]

def permutation(): #order is relevant, ex. AB and BA are different
    permList = []
    adder = findConcatenatingTerm(termList)
    for term in termList:
        tempCombo = term + adder
        count = 0
        while count < len(termList):
            tempCombo += termList[count]
            count += 1
            permList.append(tempCombo)
            tempCombo = term + adder
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

def inputList(): #doesn't need idiotProof bc no accepted values
    userList = []

    userInput = input("What's the first item in the list?\n> ")
    userList.append(userInput)
    while userInput.lower() != "done":
        userInput = input("What's the next item in the list?\nType 'done' when the list is complete.\n> ")
        userList.append(userInput)

    return userList #TEST COMMENT LOL
print(inputList())
#this is a change ig lol
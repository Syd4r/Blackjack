import random
import time
cards = random.sample(range(1, 53), 52)
comparenumber = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
cardnumber = 0
whatcard = 0
extranumber = 1
extradealer = 2
twentyonecheck = 0
twentyonecheck2 = 0
havehit = 0
def reset():
    global cardnumber
    global whatcard
    cardnumber = 0
    whatcard = 0
def whatnumber():
    global cardnumber
    global whatcard
    if cards[cardnumber] <= 4:
        whatcard = "A"
        comparenumber[cardnumber] = 11
    elif cards[cardnumber] <= 40:
        whatcard = (cards[cardnumber] + (4 -(cards[cardnumber] % 4))) / 4
        if cards[cardnumber] % 4 == 0:
            whatcard -= 1
        whatcard = int(whatcard)
        comparenumber[cardnumber] = whatcard
        whatcard = str(whatcard)
    elif cards[cardnumber] <= 44:
        whatcard = "J"
        comparenumber[cardnumber] = 10
    elif cards[cardnumber] <= 48:
        whatcard = "Q"
        comparenumber[cardnumber] = 10
    elif cards[cardnumber] <= 52:
        whatcard = "K"
        comparenumber[cardnumber] = 10
    print (whatcard, end = '  ')
    cardnumber += 1
def hiddennumber():
    global cardnumber
    global whatcard
    if cards[cardnumber] <= 4:
        whatcard = "A"
        comparenumber[cardnumber] = 11
    elif cards[cardnumber] <= 40:
        whatcard = (cards[cardnumber] + (4 -(cards[cardnumber] % 4))) / 4
        if cards[cardnumber] % 4 == 0:
            whatcard -= 1
        whatcard = int(whatcard)
        comparenumber[cardnumber] = whatcard
        whatcard = str(whatcard)
    elif cards[cardnumber] <= 44:
        whatcard = "J"
        comparenumber[cardnumber] = 10
    elif cards[cardnumber] <= 48:
        whatcard = "Q"
        comparenumber[cardnumber] = 10
    elif cards[cardnumber] <= 52:
        whatcard = "K"
        comparenumber[cardnumber] = 10
    cardnumber += 1
def playerhand():
    print ("Your Hand:")
    for i in range (0,2):
        whatnumber()
def dealerhand():
    print ("Dealer's Hand:")
    for i in range (0,1):
        hiddennumber()
    for i in range (0,1):
        whatnumber()
    print("?")
def twentyone():
    twentyonecheck = comparenumber[0]+comparenumber[1]
    for i in range (extradealer, extranumber+extradealer):
        twentyonecheck += comparenumber[i]
def twentyone2():
    for i in range (1, extradealer):
        twentyonecheck2 += comparenumber[i]
playerhand()
print (" ")
dealerhand()
print (" ")
while True:
    if comparenumber[2]+comparenumber[3] == 21:
        print ("Dealer got a blackjack, you lost!")
        break
    if comparenumber[0]+comparenumber[1] == 21:
        print ("You got a blackjack, you either won or tied!")
        break
    if havehit == 0:
        print ()
        print("Your hand total equals", comparenumber[0]+comparenumber[1], " ")
    else:
        print()
        print("Your hand total equals", twentyonecheck, " ")
    action = input("Do you want to hit or stand (H or S)?: ")
    if action == ("H"):
        havehit = 1
        reset()
        playerhand()
        for i in range (0,extradealer):
            hiddennumber()
        for i in range (0, extranumber):
            whatnumber()
        twentyone()
        extranumber += 1
        if twentyonecheck > 21:
            print ("You busted, you lost!")
            break
        if twentyonecheck == 21:
            print ("You got a 21, you either won or tied")
    if action == ("S"):
        if havehit == 0:
            print ("You ended with a", comparenumber[0]+comparenumber[1]," ")
        else:
            print("You ended with a", twentyonecheck, " ")

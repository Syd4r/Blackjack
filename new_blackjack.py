import random
import time
cards = ["A",2,3,4,5,6,7,8,9,10,"J", "Q","K","a"]
values = [11,2,3,4,5,6,7,8,9,10,10,10,10,1]
def deal(hand,cards,howmany):
    for i in range(howmany):
        hand.append(random.randint(1,13))
        hand[len(hand)-1] = cards[hand[len(hand)-1]-1]
    return hand
def showcards(hand,dealer_hand,dealer_show):
    print("Your cards are: " + str(hand))
    if dealer_show == False:
        print("The dealer has: [?, " + str(dealer_hand[1]) + "]")
    else:
        print("The dealers cards are: " + str(dealer_hand))
def bustcheck(hand,cards,values):
    busted = 0
    for i in range(len(hand)):
        busted += values[cards.index(hand[i])]
    for i in range(hand.count("A")):
        if busted > 21:
            if "A" in hand:
                hand[hand.index("A")] = "a"
                busted -= 10
    if busted > 21:
        return True
    else:
        return False
play = "balls"
while not play == "N":
    while True:
        busted = False
        play = input("Play (Y/N)?: ")
        if play == "N":
            break
        print()
        hand = []
        dealer_hand = []
        hand = deal(hand,cards,2)
        dealer_hand = deal(dealer_hand,cards,2)
        showcards(hand,dealer_hand,False)
        if values[cards.index(hand[0])] + values[cards.index(hand[1])] == 21:
            if values[cards.index(dealer_hand[0])] + values[cards.index(dealer_hand[1])] == 21:
                print("Both have 21, it's a tie!")
                break
            else:
                print("You win with 21")
                break
        elif values[cards.index(dealer_hand[0])] + values[cards.index(dealer_hand[1])] == 21:
            print("Dealer wins with 21")
            break
        while True:
            print()
            hitorstand = input("Do you want to Hit (H) or Stand (S): ")
            if hitorstand == "H":
                hand = deal(hand,cards,1)
            else:
                break
            showcards(hand, dealer_hand,False)
            busted = bustcheck(hand, cards, values)
            if busted == True:
                print("You busted")
                break
        time.sleep(2)
        print()
        showcards(hand, dealer_hand, True)
        while True:
            time.sleep(2)
            print()
            dealerhit = 0
            for i in range(len(dealer_hand)):
                dealerhit += values[cards.index(dealer_hand[i])]
            if dealerhit < 17:
                print("Dealer Hits")
                dealer_hand = deal(dealer_hand,cards,1)
                showcards(hand,dealer_hand,True)
                busted_2 = bustcheck(dealer_hand,cards,values)
                if busted_2 == True:
                    print("Dealer busted")
                    if busted == True:
                        print("Its a Tie")
                    if busted == False:
                        print("You Win")
                    break
            else:
                print("Dealer stands")
                showcards(hand,dealer_hand,True)
                dealerhit = 0
                for i in range(len(dealer_hand)):
                    dealerhit += values[cards.index(dealer_hand[i])]
                handcompare = 0
                for i in range(len(hand)):
                    handcompare += values[cards.index(hand[i])]
                if handcompare > 21:
                    print("Dealer Wins")
                    break
                if dealerhit > handcompare:
                    print("Dealer Wins")
                elif dealerhit == handcompare:
                    print("It's a tie")
                else:
                    print("You win!")
                break

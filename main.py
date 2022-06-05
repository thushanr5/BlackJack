#blackjack (21)
#name
import random

deck = []
myHand = []
dealerHand = []
userTotal = 0
dealerTotal = 0

#create card object
class Card:

	def _init_(self):
		self.suit = ""
		self.face = ""
		self.value = 0


def createDeck ():

	suits = ["Clubs", "Spades", "Hearts", "Diamonds"]	
	faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

	#use for loops to create all 52 cards in the deck

	for x in range(4): #suits loop 
		for y in range(13):  #faces loop

			c = Card()
			c.suit = suits[x]
			c.face = faces[y]
			c.value = y + 1

			if (y > 9):      #takes care of JQK
				c.value = 10
			if (y == 0):			#takes care of A = 11
				c.value = 11

			deck.append(c)
		#	print(c.suit + "  " + c.face + "  " +str(c.value))

	random.shuffle(deck)


def dealUser():
	global userTotal
	myHand.append(deck[0])
	del(deck[0])
	# add last card put in hand to the userTotal
	userTotal += myHand[len(myHand) - 1].value

def dealDealer():
	global dealerTotal
	dealerHand.append(deck[0])
	del(deck[0])
	# add last card put in dealer hand to dealerTotal
	dealerTotal += dealerHand[len(dealerHand) - 1].value


#CHALLENGE################################################
#try to make ONE function that could deal to either player
def dealSomebody(who):
	if (who == "user"):
		myHand.append(deck[0])
		dealUser()
	else:
		#dealerHand.append(deck[0])
		dealDealer()

	del(deck[0])

def printUserCards():	
	print("\n\nMy Cards")
	for x in range(len(myHand)):
		print(myHand[x].face + " " + myHand[x].suit)

def printDealerCards():
	print("\n\nDealer Cards")
	for x in range(len(dealerHand)):
		print(dealerHand[x].face + " " + dealerHand[x].suit)




def main():
	print("Welcome to the Blackjack Game!")
	createDeck()

	#initial deal
	dealUser()
	dealUser()
	dealDealer()
	dealDealer()
	printUserCards()
	printDealerCards()

	#game play
	#user turn first
	while (True):          #True makes in infinite loop
		choice = input("Do you want to hit or stand?")
		
		if (choice == "stand" or choice == "Stand"):    
			break
		elif (choice == "hit"):
			dealUser()

		printUserCards()


	while (dealerTotal < 17):
		dealDealer()
		printDealerCards()
    
main()

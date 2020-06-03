import os, math

VERSION = "Pre-pre 0.0.1"

def updateScreen(Log=False):
	os.system("cls")
	print("Secret Hitler Probability Calculator\nVersion: {}\n".format(VERSION))

class Game:
	"""Monolith class for calculator"""
	DeckCards = []
	Board = []
	Discard = []
	Log = []
	# Deck Cards = Current cards in deck
	# Board = Cards on board in order
	# Discard = Cards in discard zone
	# Log = Game Log
	LibCards = 0
	FascCards = 0
	DeckCardsNum = 0
	ConstL = 0
	ConstF = 0
	ConstDeck = 0
	# Lib Cards = Current liberal cards
	#  FascCards = Current fasc cards
	# DeckCardsNum = Current num of cards
	# ConstL, ConstF, ConstDeck = Initially nums of var

	def __init__(self, LibC=6, FascC=11):
		# super(Calculator, self).__init__()
		self.LibCards = self.ConstL= LibC
		self.FascCards = self.ConstF = FascC
		self.DeckCardsNum = self.ConstDeck = self.LibCards + self.FascCards
		self.updateScreen(False)

	def claim(self):
		claims = input("Example of usage: Brown Green FFL FL L\n").split()
		self.Log.append("{} > {}: {} > {} > {}\n".format(claims[0], claims[1], claims[2], claims[3], claims[4]))
		self.updateCards(claims[2], claims[3], claims[4])
		self.updateScreen()

	def deleteLine(self):
		self.Log.pop(int(input("Enter line num to del: "))-1)
		self.updateScreen()

	def execute(self, command):
		if command == 'give':
			self.claim()
		elif command == "del":
			self.deleteLine()
		elif command == "deck":
			self.updateScreen()
			print("Deck: {}L, {}F\nCurrent deck: {}L, {}F".format(self.ConstL, self.ConstF, self.LibCards, self.FascCards))
	def updateScreen(self, Log=True):
		os.system("cls")
		print("Secret Hitler Probability Calculator\nVersion: {}\n".format(VERSION))
		if Log:
			self.getBoard()
			self.getCurrentDeck()
			self.getLog()

	def getLog(self):
		for line in self.Log:
			print(line)

	def getCurrentDeck(self):
		print("Current deck: {}L, {}F\n".format(self.LibCards, self.FascCards))

	def getBoard(self):
		print("Board: ", end='')
		for card in self.Board:
			print(card, end='')
		print()

	def updateCards(self, pres, chan, choice):
		for card in pres:
			if card.upper() == "L":
				self.LibCards -= 1
			elif card.upper() == "F":
				self.FascCards -= 1
		self.Board.append(choice)

def main():
	game = Game(7, 13)
	command = str()
	while command != "q":
		command = input()
		game.execute(command)
	exit(0)


if __name__ == '__main__':
	main()
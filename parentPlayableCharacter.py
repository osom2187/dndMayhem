from random import randint


class PlayableCharacter:

    def __init__(self, name='botName', hitpoints=10, shieldsInFront=0, cardsInHand=3, cardsInDeck=20, actionsRemaining=1):
        self.__name = name
        self.__hitpoints = hitpoints
        self.__shieldsInFront = shieldsInFront
        self.__cardsInHand = cardsInHand
        self.__cardsInDeck = cardsInDeck
        self.__actionsRemaining = actionsRemaining

    def __getName(self):
        return self.__name

    def __setName(self, name):
        self.__name = name

    name = property(__getName, __setName)

    def __getHitpoints(self):
        return self.__hitpoints

    def __setHitpoints(self, hitpoints):
        self.hitpoints = hitpoints

    hitpoints = property(__getHitpoints, __setHitpoints)

    def __getShieldsInFront(self):
        return self.__shieldsInFront

    def __setShieldsInFront(self, shieldsInFront):
        self.shieldsInFront = shieldsInFront

    shieldsInFront = property(__getShieldsInFront, __setShieldsInFront)
    def __getCardsInHand(self):
        return self.__cardsInHand

    def __setCardsInHand(self, cardsInHand):
        self.cardsInHand = cardsInHand

    cardsInHand = property(__getCardsInHand, __setCardsInHand)

    def __getCardsInDeck(self):
        return self.__cardsInDeck

    def __setCardsInDeck(self, cardsInDeck):
        self.cardsInDeck = cardsInDeck

    cardsInDeck = property(__getCardsInDeck, __setCardsInDeck)

    def __getActionsRemaining(self):
        return self.__actionsRemaining

    def __setActionsRemaining(self, actionsRemaining):
        self.actionsRemaining = actionsRemaining

    actionsRemaining = property(__getActionsRemaining, __setActionsRemaining)

    # standard methods

    def __str__(self):
        return f'{self.name} has {self.hitpoints} hitpoints and {self.shieldsInFront} shields out on the battlefield'

    # functionalities
    def shuffleDeck(self):
        self.cardsInDeck = []
        for x in range(1, 21):
            self.cardsInDeck.append(randint(1, 21))

    def deathCheck(self, attackDmg):
        if self.hitpoints - (attackDmg - self.shieldsInFront) <= 0:
            return f'Unfortunately {self.name} has died on the battlefield.'

    def getAttacked(self, attackDmg):
        if self.shieldsInFront == 0:
            self.__hitpoints = self.__hitpoints - attackDmg
            self.deathCheck(attackDmg)
        else:
            self.hitpoints = self.hitpoints - (attackDmg - self.shieldsInFront)
            self.deathCheck(attackDmg)
            if self.shieldsInFront - attackDmg <= 0:
                self.shieldsInFront = 0
            else:
                self.shieldsInFront = self.shieldsInFront - attackDmg

    def healUp(self, healingReceived):
        self.__hitpoints = self.__hitpoints + healingReceived
        if self.__hitpoints > 10:
            self.__hitpoints = 10

    def drawCards(self, numOfCards):
        counter = [range(0, numOfCards+1)]
        self.cardsInHand = self.cardsInHand + self.cardsInDeck[counter]
        self.cardsInDeck = self.cardsInDeck[counter[:-1]:]

    def lookAtHand(self): # the variable playersDeck is defined in the childclass pc*playable character's name*
        for card in self.cardsInHand:
            f'You have card number {card} ({playersDeck[card]}) on your hand'
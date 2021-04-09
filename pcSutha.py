from characterClasses.parentPlayableCharacter import PlayableCharacter


class Sutha(PlayableCharacter):

    def __init__(self, name='Sutha', hitpoints=10, shieldsInFront=0, cardsInHand=3, cardsInDeck=20, actionsRemaining=1): #showCard=int(input('Which card shall I show you(enter cardNum)'))):
        PlayableCharacter.__init__(self, name, hitpoints, shieldsInFront, cardsInHand, cardsInDeck, actionsRemaining)
        #self.showCard = showCard

# getter setter property

    def __getShowCard(self):
        return self.showCard

    def __setShowCard(self, showCard):
        self.showCard = showCard

    showCard = property(__getShowCard, __setShowCard)

# standard method

    def __str__(self):
        return f'{self.name} has {self.hitpoints} hp and {self.shieldsInFront} shields out on the battlefield.'

# functionalities

    def suthasDeck(self, num):
        suthasCards = {
        1:{
            'Brutal Punch':-2
            },
        2:{
            'Brutal Punch':-2
        },
        3:{
            'Big Axe Is Best Axe':-3
        },
        4:{
            'Big Axe Is Best Axe':-3
        },
        5:{
            'Big Axe Is Best Axe':-3
        },
        6: {
            'Big Axe Is Best Axe': -3
        },
        7: {
            'Big Axe Is Best Axe': -3
        },
        8:{
            'Rage':-4
        },
        9:{
            'Rage':-4
        },
        10:{'''
            'Flex!':[sutha.healUp(1), sutha.drawCards(1)]
        },
        11:{
            'Snack Time':[sutha.healUp(1), sutha.drawCards(2)]
        },
        12:{
            'Open The Armory':sutha.drawCards(2)
        },
        13:{
            'Open The Armory':sutha.drawCards(2)
        },
        14:{
            'Bag Of Rats':[sutha.drawCards(1), sutha.shieldsInFront(1)]
        },
        15:{
            'Spiked Shield':sutha.shieldsInFront(2)
        },
        16:{
            'Raff':sutha.shieldsInFront(3)
        },
        17:{
            'Riff':sutha.shieldsInFront(3)
        },
        18:{
            'Two Axes Are Better Than One':sutha.actionsRemaining(+2)
        },
        19:{
            'Two Axes Are Better Than One':sutha.actionsRemaining(+2)
        },
        20:{
            'Head Butt':[-1, sutha.actionsRemaining(+1)]
        },
        21:{
            'Head Butt': [-1, sutha.actionsRemaining(+1)]
        },
        22:{# need to figure out how to deal the damage to each opponent
            'Whirling Axes': [-1, sutha.healUp(input('How many players are in the game?:'))]
        },
        23:{# need to figure out how to deal the damage to each opponent
            'Whirling Axes': [-1, sutha.healUp(input('How many players are in the game?:'))]
        },
        24:{# need to figure out how to select an opponents shield card
            'Mighty Toss': ['placeholder', sutha.drawCards(1)]
        },
        25:{# need to figure out how to select an opponents shield card
            'Mighty Toss': ['placeholder', sutha.drawCards(1)]
        },
        26:{# need to discard everyones hand
            'BattleRoar':[sutha.actionsRemaining(+1), 'placeholder']
        },
        27:{# need to discard everyones hand
            'BattleRoar':[sutha.actionsRemaining(+1), 'placeholder']'''
        }}
        print(suthasCards[num])



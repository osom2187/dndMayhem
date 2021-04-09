from characterClasses.parentPlayableCharacter import PlayableCharacter


class Lia(PlayableCharacter):

    def __init__(self, name='Lia'):
        PlayableCharacter.__init__(self, name)

    # get set prop

    # standard method

    def __str__(self):
        return f'{self.name} has {self.hitpoints} hp and {self.shieldsInFront} shields out on the battlefield.'

    # functionalities

    def liasDeck(self, num):
        liasCards = {}
        print(liasCards[num])
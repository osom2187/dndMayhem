class DungeonMaster:
    def preGameDialog(questionP1=input('Whom would you like to play, Player One?')):
        remainingCharacters = ['Sutha', 'Lia', 'Azzan', 'Oriax']
        if questionP1 == 'Sutha':
            remainingCharacters = remainingCharacters[1:]
            print('Player chose big Sutha, is best choice!')
        elif questionP1 == 'Lia':
            remainingCharacters = [remainingCharacters[0], remainingCharacters[2], remainingCharacters[3]]
            print('I shall do justice in your name, master player!')
        elif questionP1 == 'Azzan':
            remainingCharacters = [remainingCharacters[0], remainingCharacters[1], remainingCharacters[3]]
            print('Let\'s fireball them all while nobody is looking!')
        elif questionP1 == 'Oriax':
            remainingCharacters = remainingCharacters[:3]
            print('Hey player person, don\'t you worry about a thing I already know how to \'sneak attack\'.')
        else:
            print('Hmmm, I am a droid so don\'t get angry but I did not understand what you want from me.')
        print('The remaining characters are:', remainingCharacters)


#def playACard():



#def giveUp():
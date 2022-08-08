import random
import time

suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
ranks = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11,
    }


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    deck = []
    for keys, values in ranks.items():
        for suit in suits:
            card = Card(keys, suit)
            deck.append(card)

    def get_deck(self):
        return self.deck


class Player:
    def __init__(self, name, card1, card2):
        self.name = name
        self.card1 = card1
        self.card2 = card2

    def get_info(self):
        return f'Hello, {self.name}\nYour cards:\nCard 1:{self.card1}\nCard 2:{self.card2}'



def new_game():
    print('New game?(y/n)')
    answer = input()
    if answer == 'y':
        deck = Deck()
        player = Player(input('what is your name:'), random.sample(deck.get_deck(), 1)[0],
                        random.sample(deck.get_deck(), 1)[0])

        print(player.get_info())

        score = ranks[player.card1.rank] + ranks[player.card2.rank]
        print('Your score is:', score, '\nDo you want to grab another card?(y/n)')
        answer_card = input()
        if answer_card == 'y':
            card_3 = random.sample(deck.get_deck(), 1)[0]
            print(f'Your third card is {card_3.rank} of {card_3.suit}')
            score += ranks[card_3.rank]
            print(f'Now your score is: {score}')
            if score < 21:
                another_answer = input('Another one card? (y/n)')
                if another_answer == 'y':
                    card_4 = random.sample(deck.get_deck(), 1)[0]
                    print(f'Your third card is {card_4.rank} of {card_4.suit}')
                    score += ranks[card_4.rank]
                    print(f'Now your score is: {score}')
                elif another_answer == 'n':
                    print(f'Now your score is: {score}')
                else:
                    print('Error. Unknown command')
            else:
                print('You lost')
        elif answer_card == 'n':
            print(f'Okay, your score is: {score}')
        else:
            print('Unknown Command, quiting...')

        
    elif answer == 'n':
        print('okay')
    else:
        print('Error: Unknown command')

    score_2 = score

    def dealer_time():
        dealer = Player('Dealer', random.sample(deck.get_deck(), 1)[0],
                        random.sample(deck.get_deck(), 1)[0])
        dealer_score = score = ranks[dealer.card1.rank] + ranks[dealer.card2.rank]
        print(dealer.get_info()+'\n'+f'Dealer"s score is: {dealer_score}')
        if dealer_score <= 16:
            print('Thinking about taking another card...')
            time.sleep(4)
            dealers_card_3 = random.sample(deck.get_deck(), 1)[0]
            print(f'Your third card is {dealers_card_3.rank} of {dealers_card_3.suit}')
            dealer_score += ranks[dealers_card_3.rank]
            print(f"Dealer's score: {dealer_score}")
        return dealer_score

    if score_2 <= 21:
        x = dealer_time()
        if int(x) >= score_2:
            print('\n')
            print('ti_hui')
        else:
            print('\n')
            print('on hui')





new_game()







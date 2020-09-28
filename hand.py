import random


class Hand:
    player_wins = 0
    house_wins = 0

    def __init__(self):
        self.cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.hand = 0
        self.natural = False
        self.turn = False
        self.hit = 0
        self.three_cards = False
        self.bonus = False

    def clear(self):
        self.hand = 0
        self.natural = False
        self.turn = False
        self.three_cards = False
        self.bonus = False

    def draw(self):
        card_index = random.randint(0, 12)
        card = self.cards[card_index]
        self.hand += card
        if self.hand >= 10:
            self.hand -= 10

        return card

    def natural_win(self):
        if self.hand == 9 or self.hand == 8:
            self.natural = True
            return True
        else:
            return False


class Player(Hand):
    def __init__(self):
        self.bet = 0
        self.bank = 10000
        self.max_bet = 10000
        self.dragon = 0
        self.panda = 0
        self.house = False
        self.player = False
        Hand.__init__(self)

    def check_bet(self, bet):
        if self.bank < bet:
            print("You don't have enough money for this bet")
            return False
        elif bet > self.max_bet:
            print("Bet cannot be greater than", self.max_bet)
        elif bet % 5 == 0:
            return True
        else:
            print("Bet must be a multiple of five")
            return False

    def clear_bets(self):
        self.house = False
        self.player = False

    def place_panda(self):
        get_panda = True
        while get_panda:
            print("You have $", player.bank)
            try:
                place_panda = int(input("How much would you like to bet on Panda? "))
                if self.check_bet(place_panda):
                    self.panda = place_panda
                    self.bank -= place_panda
                    get_panda = False
                else:
                    get_panda = True
            except:
                ValueError

    def place_dragon(self):
        get_dragon = True
        while get_dragon:
            print("You have $", player.bank)
            try:
                place_dragon = int(input("How much would you like to bet on Dragon? "))
                if self.check_bet(place_dragon):
                    self.dragon = place_dragon
                    self.bank -= place_dragon
                    get_dragon = False
                else:
                    get_dragon = True
            except:
                ValueError

    def place_base_bet(self):
        if self.bank < 5:
            print("You lost all your money! Better luck next time.")
            exit(-1)  # is exit -1 enough to exit whole program?
        get_base_bet = True
        while get_base_bet:
            print("You have $", player.bank)
            print("House:", Hand.house_wins, "Player:", Hand.player_wins)
            try:
                place_base = int(input("How much would you like to place on the base bet? "))
                if place_base == 0:
                    print("Base bet must be at least $5")
                    get_base_bet = True
                elif self.check_bet(place_base):
                    self.bet = place_base
                    self.bank -= place_base
                    get_base_bet = False
                    betting_for = True
                    while betting_for:
                        print("Would you like to bet on House or Player?")
                        try:
                            bet_for = int(input("'1' bets for House. '2' bets for Player. "))
                            if bet_for == 1:
                                self.house = True
                                betting_for = False
                            elif bet_for == 2:
                                self.player = True
                                betting_for = False
                            else:
                                betting_for = True
                        except:
                            ValueError
                else:
                    get_base_bet = True
            except:
                ValueError



player = Player()
house = Hand()

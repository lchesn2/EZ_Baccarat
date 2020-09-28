import hand
from hand import Hand, player, house


def house_when_player_hits():
    if 0 <= house.hand < 3:
        print("House hits draws", house.draw())
        if house.hand == 7:
            house.bonus = True
        check_hands()
    elif house.hand == 3 and player.hit != 8:
        print("House hits draws", house.draw())
        if house.hand == 7:
            house.bonus = True
        check_hands()
    elif house.hand == 4 and 1 < player.hit < 8:  # hits on 2-7
        print("House hits draws", house.draw())
        if house.hand == 7:
            house.bonus = True
        check_hands()
    elif house.hand == 5 and 3 < player.hit < 8:
        print("House hits draws", house.draw())
        if house.hand == 7:
            house.bonus = True
        check_hands()
    elif house.hand == 6 and (house.hit == 6 or house.hit == 7):
        print("House hits draws", house.draw())
        if house.hand == 7:
            house.bonus = True
        check_hands()
    else:
        check_hands()


def dragon():
    print("Dragon!!!!")
    print("-----[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]-----")
    print("-----[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]-----")
    print("-----[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]-----")
    dragon_winning = player.dragon * 40
    print("You win", dragon_winning)
    dragon_winning += player.dragon
    player.bank += dragon_winning


def panda():
    print("Panda!!!!")
    print("!!!-----[̲̅$̲̅(̲̅ιοο̲̅)̲̅$̲̅]-----!!!")
    panda_winning = player.panda * 25
    print("You win", panda_winning)
    panda_winning += player.panda
    player.bank += panda_winning


def check_hands():
    if house.hand > player.hand:
        Hand.house_wins += 1
        if house.bonus:
            dragon()
        if player.house:
            player.bank += player.bet * 2
            print("You bet House. Player:", player.hand, "House:", house.hand)
        else:
            print("You bet player. Player:", player.hand, "House:", house.hand)

    elif player.hand > house.hand:
        Hand.player_wins += 1
        if player.bonus:
            panda()
        if player.player:
            player.bank += player.bet * 2
            print("You bet Player. Player:", player.hand, "House:", house.hand)
        else:
            print("You bet House. Player:", player.hand, "House:", house.hand)

    else:
        print("Push. Player:", player.hand, "House:", house.hand)
        player.bank += player.bet
    house.clear()
    player.clear()
    player.clear_bets()


def user_interface():
    print("Welcome to EZ Baccarat")
    beginning = True
    while beginning:
        print("\n")
        print('New hand, place your bets in multiples of five')
        player.place_base_bet()
        player.place_panda()
        player.place_dragon()
        player.draw()
        house.draw()

        player.draw()
        house.draw()

        print("Player's hand is", player.hand)
        print("House's hand is", house.hand)
        beginning = False
        player.turn = True
        if player.natural_win() or house.natural_win():
            player.turn = False
            house.turn = False
            check_hands()
            beginning = True
        while player.turn:
            if player.hand == 6 or player.hand == 7:
                print("Player stays")
                if house.hand == 6 or house.hand == 7:
                    player.turn = False
                    house.turn = False
                    check_hands()
                    beginning = True
                else:
                    print("House hits draws", house.draw())
                    if house.hand == 7:
                        house.bonus = True
                    player.turn = False
                    house.turn = True
                    check_hands()
                    beginning = True
            elif 0 <= player.hand < 6:
                player.hit = player.draw()
                print("Player hits draws", player.hit)
                if player.hand == 8:
                    player.bonus = True
                player.turn = False
                house.turn = True
            if house.turn:
                house_when_player_hits()
                beginning = True

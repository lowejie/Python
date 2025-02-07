import random

game_on = True


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player = []
    computer = []
    player_draw_count = 0
    cpu_draw_count = 0

    def deal_card(user):
        card = random.choice(cards)
        user.append(card)

    def start_game(user):
        while len(user) != 2:
            deal_card(user)

    def show_cards(user, cpu):
        print(f"Your cards: {user}, current score: {sum(user)}")
        print(f"Computer's first card: {cpu[0]}")

    def show_final(user, cpu):
        print(f"Your final hand: {user}, final score: {sum(user)}")
        print(f"Computer's final hand: {cpu}, final score:{sum(cpu)}")

    def replace11(user):
        if sum(user) > 21 & 11 in user:
            user.remove(11)
            user.append(1)

    def check_cards(user, cpu):
        if sum(user) > 21:
            show_final(user, cpu)
            print("You went over. Lose.")
        elif sum(cpu) > 21:
            show_final(user, cpu)
            print("CPU went over. Win.")
        elif sum(cpu) > sum(user):
            show_final(user, cpu)
            print("CPU more. Lose.")
        elif sum(user) > sum(cpu):
            show_final(user, cpu)
            print("You more. Win.")
        else:
            show_final(user, cpu)
            print("Draw.")

    start_game(player)
    start_game(computer)
    show_cards(player, computer)
    while input("Type 'y' to get another card, type any other to pass: ") == 'y':
        deal_card(player)
        player_draw_count += 1
        replace11(player)
        show_cards(player, computer)
        if sum(player) > 21:
            check_cards(player, computer)
            return
        elif player_draw_count == 5:
            break
    while sum(computer) < 17:
        deal_card(computer)
        cpu_draw_count += 1
        replace11(computer)

    check_cards(player, computer)


while game_on:
    game_start = input("Do you wanna play a game of Blackjack? Type 'y' or 'n': ")
    if game_start == 'y':
        blackjack()
    elif game_start == 'n':
        game_on = False
        print("Game session ended.")

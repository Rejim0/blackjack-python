import random
import art

# deal random card
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# calculate score
def calculate_score(cards):
    # check blackjack
    if len(cards) == 2 and sum(cards) == 21:
        return 0

    # change Ace from 11 to 1 if over 21
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


# compare scores
def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "You lose"
    elif u_score == 0:
        return "You win"
    elif u_score > 21:
        return "You lose"
    elif c_score > 21:
        return "You win"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"


def play():
    print(art.logo)
    user_card = []
    computer_card = []
    is_game_over = False

    # give 2 cards each
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    # user turn
    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"\nYour cards: {user_card}, current score: {user_score}")
        print(f"Computer first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    # computer turn
    computer_score = calculate_score(computer_card)
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    # recalculate final scores
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    # final result
    print("\nFinal result:")
    print(f"Your final cards: {user_card}, final score: {user_score}")
    print(f"Computer final cards: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    play()
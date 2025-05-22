import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    """Calculates the score of the given hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack!
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print("Welcome to Blackjack!")

    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")
            if should_continue == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))

if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()
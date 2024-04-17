from art import logo
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(cards=cards):
    random_card = random.choice(cards)
    return random_card


def calculate_score(list_of_cards):
    result = sum(list_of_cards)
    if 11 in list_of_cards and result > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        return sum(list_of_cards)
    if len(list_of_cards) == 2 and result == 21:
        return 0
    else:
        return result


def compare(user_score, computer_score):
    if user_score == computer_score:
        return f"DRAW😐\ncomputer final hand:{computer_cards} final score:{sum(computer_cards)}\nyour final hand:{user_cards} final score:{sum(user_cards)}"
    elif user_score == 0:
        return f"YOU WIN😃\ncomputer final hand:{computer_cards} final score:{sum(computer_cards)}\nyour final hand:{user_cards} final score:{sum(user_cards)}"
    elif computer_score == 0:
        return f"COMPUER WIN☹️\ncomputer final hand:{computer_cards} final score:{sum(computer_cards)}\nyour final hand:{user_cards} final score:{sum(user_cards)}"
    elif user_score > 21:
        return f"COMPUTER WIN☹️\ncomputer final hand:{computer_cards} final score:{sum(computer_cards)}\nyour final hand:{user_cards} final score:{sum(user_cards)}"
    elif computer_score > 21:
        return f"YOU WIN😃\ncomputer final hand:{computer_cards} final score:{sum(computer_cards)}\nyour final hand:{user_cards} final score:{sum(user_cards)}"
    elif computer_score > user_score:
        return f"COMPUTER WIN☹️\ncomputer final hand:{computer_cards} final score:{sum(computer_cards)}\nyour final hand:{user_cards} final score:{sum(user_cards)}"
    else:
        return f"YOU WIN😃\ncomputer final hand:{computer_cards} final score:{sum(computer_cards)}\nyour final hand:{user_cards} final score:{sum(user_cards)}"


user_cards = []
computer_cards = []


def game():
    print(logo)
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(f"your cards: {user_cards} current score:{sum(user_cards)}")
    print(f"computer first card {computer_cards[0]}")

    while calculate_score(user_cards) != 0 or calculate_score(computer_cards) != 0 or calculate_score(user_cards) <= 21:
        ask = input("Type 'y' to anoher card, type 'n' to pass: ")
        if ask == "y":
            user_cards.append(deal_card())
            if calculate_score(user_cards) > 21:
                break
            print(f"your cards: {user_cards} current score:{sum(user_cards)}")
        else:
            while calculate_score(computer_cards) < 17:
                computer_cards.append(deal_card())
            break

    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))


game()
while True:
    user_cards = []
    computer_cards = []
    answer = input("Do you want to play again ? Type 'yes' or 'no': ")
    if answer == "yes":
        os.system("cls")
        game()
    else:
        break

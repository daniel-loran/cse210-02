from random import randint

points = 300

again = "y"

while again == "y":

    cards = randint(1,13)
    present_card = randint(1,13)

    print(f"The card is: {present_card}")
    h_or_l = (input(f"Higher or lower? [h/l]: "))
        
    if present_card < cards and h_or_l == "h":
            print(f"Next card was: {cards}")
            points += 100
            print(f"Your Score Is: {points}")
            again = input("Play again? [y/n]")
    elif present_card > cards and h_or_l == "l":
            print(f"Next card was: {cards}")
            points += 100
            print(f"Your Score Is: {points}")
            again = input("Play again? [y/n]")
    else:
            print(f"Next card was: {cards}")
            points -= 75
            print(f"Your Score Is: {points}")
            again = input("Play again? [y/n]")
    print("")
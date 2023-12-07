hands = []


def init_hands(input):
    input = input.translate(str.maketrans("TJQKA", "ABCDE")).split("\n")
    for line in input:
        cards, bid = line.split()
        hands.append({
            "cards": cards,
            "bid": int(bid),
        })


def get_point(cards):
    return sum(cards.count(card) for card in cards)


def get_point_joker(cards):
    options = [cards.replace("B", card) for card in cards if card != "B"]
    if not options:
        return 25
    return max(get_point(option) for option in options)


def solution_1():
    hands.sort(key=lambda hand: (get_point(hand["cards"]), hand["cards"]))
    return sum(rank * hand["bid"] for rank, hand in enumerate(hands, 1))


def solution_2():
    hands.sort(key=lambda hand: (get_point_joker(hand["cards"]), hand["cards"].replace("B", "0")))
    return sum([rank * hand["bid"] for rank, hand in enumerate(hands, 1)])


if __name__ == "__main__":
    input = open("input.txt").read()
    init_hands(input)
    print(solution_1())
    print(solution_2())

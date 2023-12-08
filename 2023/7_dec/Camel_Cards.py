with open("input.txt") as f:
    info = f.read().splitlines()

hands = [hand.split() for hand in info]

value_cards = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 0,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1
}


def hand_value(hand):
    ammount = []
    for key in value_cards.keys():
        ammount.append(hand.count(key))
    jokers = ammount.pop(3)
    ammount[ammount.index(max(ammount))] += jokers
    if ammount.count(5) == 1:
        return 7
    elif ammount.count(4) == 1:
        return 6
    elif ammount.count(2) == 1 and ammount.count(3) == 1:
        return 5
    elif ammount.count(3) == 1:
        return 4
    elif ammount.count(2) == 2:
        return 3
    elif ammount.count(2) >= 1:
        return 2
    else:
        return 1


order = []
while len(hands) > 0:
    low_hand = hands[0]
    for hand in hands:
        if hand_value(hand[0]) < hand_value(low_hand[0]):
            low_hand = hand
        elif hand_value(hand[0]) == hand_value(low_hand[0]):
            for i in range(5):
                if value_cards[hand[0][i]] < value_cards[low_hand[0][i]]:
                    low_hand = hand
                    break
                elif value_cards[hand[0][i]] > value_cards[low_hand[0][i]]:
                    break
    order.append(low_hand)
    hands.pop(hands.index(low_hand))

score = 0
for i, cards in enumerate(order):
    score += int(cards[1]) * (i + 1)

print(score)
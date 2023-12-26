CARD_VALUES = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 11,
    "K": 12,
    "A": 13,
}


class Hand:

    def __init__(self, line):
        self.hand_string = line.split()[0]
        self.bid = int(line.split()[1])
        self.count = self.hand_count()
        self.hand_type()

    def hand_count(self):
        count = {}
        count["J"] = 0
        for c in self.hand_string:
            if c not in count:
                count[c] = 0
            count[c] += 1
        self.jokers = count["J"]
        count["J"] = 0
        return count

    def hand_type(self):
        count_v = list(self.count.values())
        c5 = count_v.count(5)
        c4 = count_v.count(4)
        c3 = count_v.count(3)
        c2 = count_v.count(2)
        c1 = count_v.count(1)
        j = self.jokers
        if (c5 == 1 or (c4 == 1 and j == 1) or (c3 == 1 and j == 2) or (c2 == 1 and j == 3) or (c1 == 1 and j == 4) or j == 5):
            # XXXXX, XXXXJ, XXXJJ, XXJJJ, XJJJJ
            # self.type = 'five_of_a_kind'
            self.strength = 6
            return
        if ((c4 == 1) or (c3 == 1 and j == 1) or (c2 == 1 and j == 2) or (j == 3)):
            # XXXXY, XXXJY, XXJJY, XJJJY
            # self.type = 'four_of_a_kind'
            self.strength = 5
            return
        if ((c3 == 1 and c2 == 1) or (c2 == 2 and j == 1)):
            # XXXYY, XXYYJ
            # self.type = 'full_house'
            self.strength = 4
            return
        if ((c3 == 1 and c1 == 2) or (c2 == 1 and c1 == 2 and j == 1) or (c1 == 3 and j == 2)):
            # XXXYZ, XXYZJ, XYZJJ 
            # self.type = 'three_of_a_kind'
            self.strength = 3
        if ((c2 == 2 and c1 == 1)):
            # XXYYZ
            # self.type = 'two_pairs'
            self.strength = 2
        if ((c2 == 1 and c1 == 3) or (c1 == 4 and j == 1)):
            # XXYZA, #XYZAJ
            # self.type = 'one_pair'
            self.strength = 1
        if (c1 == 5):
            # self.type = 'high_card'
            self.strength = 0

    def __str__(self):
        return f"{self.hand_string}, {self.strength} {self.bid}"

    def __eq__(self, other):
        if self.strength == other.strength:
            for s, o in zip(self.hand_string, other.hand_string):
                if s != o:
                    return False
            return True
        return False

    def __lt__(self, other):
        if self.strength == other.strength:
            for s, o in zip(self.hand_string, other.hand_string):
                if s == o:
                    continue
                if CARD_VALUES[s] < CARD_VALUES[o]:
                    return True
                if CARD_VALUES[s] > CARD_VALUES[o]:
                    return False
            return False
        return self.strength < other.strength

    def __gt__(self, other):
        if self.strength == other.strength:
            for s, o in zip(self.hand_string, other.hand_string):
                if s == o:
                    continue
                if CARD_VALUES[s] > CARD_VALUES[o]:
                    return True
                if CARD_VALUES[s] < CARD_VALUES[o]:
                    return False
            return False
        return self.strength > other.strength


def main():
    with open("07/input.txt", "r") as f:
        hands = []
        for line in f:
            hands.append(Hand(line))
        hands = sorted(hands)
        total_winnings = 0
        for rank, hand in enumerate(hands):
            print(hand)
            total_winnings += hand.bid*(rank+1)
        print(total_winnings)


if __name__ == "__main__":
    main()

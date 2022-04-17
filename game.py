from random import randint


class Card:
    COUNT_NUMBERS = 15

    @staticmethod
    def set_one_string_for_card(appended_numbers):
        card_string = list(randint(1, 90) for i in range(5))
        card_string = sorted(card_string)

        for i in range(len(card_string)):
            while card_string[i] in appended_numbers:
                card_string[i] = randint(1, 90)
            appended_numbers.append(card_string[i])

        card_string = sorted(card_string)

        for i in range(4):
            card_string.insert(randint(0,6), " ")

        return card_string, appended_numbers

    def __init__(self):
        self.numbers = []
        appended_numbers = []
        for i in range(3):
            card_string, appended_numbers = self.set_one_string_for_card(appended_numbers)
            self.numbers.append(card_string)

    def get_one_list(self):
        return self.numbers[0]+self.numbers[1]+self.numbers[2]


class Player:

    def __init__(self, card: Card, player_number=1, computer=True, win=False):
        self.computer = computer
        self.card = card
        self.player_number = player_number
        self.win = win

    def __str__(self):
        return f'---{f"Карточка компьютера {self.player_number}" if self.computer else f"-Карточка игрока {self.player_number}-"}---\n' \
               f'{"".join(" " + str(i) + " " if len(str(i))==1 else str(i)+ " " for i in self.card.numbers[0]) }\n' \
               f'{"".join(" " + str(i) + " " if len(str(i))==1 else str(i)+ " " for i in self.card.numbers[1]) }\n' \
               f'{"".join(" " + str(i) + " " if len(str(i))==1 else str(i)+ " " for i in self.card.numbers[2]) }\n'\
               f'---------------------------'

    def __repr__(self):
        return f"Компьютер {self.player_number}" if self.computer else f"Игрок {self.player_number}"

    def computer_turn(self, number):
        for i in range(3):
            if number in self.card.numbers[i]:
                for k in range(9):
                    if self.card.numbers[i][k] == number:
                        self.card.numbers[i][k] = "-"
                        self.card.COUNT_NUMBERS -= 1
                        break
        if self.card.COUNT_NUMBERS == 0:
            self.win = True
        return True if self.card.COUNT_NUMBERS == 0 else False

    def player_turn(self, number, answer):

        if number not in self.card.get_one_list() and answer == "y" or number in self.card.get_one_list() and answer == "n":
            return f"Игрок {self.player_number} проиграл!"

        return self.computer_turn(number)


def play(player1, player2, player_type):
    win = False
    elongated_bochki = []
    bochki = 90
    while not win:

        number = randint(1, 90)
        while number in elongated_bochki:
            number = randint(1, 90)
        elongated_bochki.append(number)
        bochki -=1
        print(f"    Бочонок номер {number} (осталось {bochki})")

        if player_type == 1:
            print(player2)
            print(player1)
            print("Зачеркнуть цифру? (y/n)")
            answer = input()
            win = player1.computer_turn(number) or player2.player_turn(number, answer)
        elif player_type == 2:
            print(player2)
            print("Зачеркнуть цифру? (y/n)")
            answer = input()
            win = player2.player_turn(number, answer)

            if win:
                if player2.win:
                    return f"Выиграл {repr(player2)}"
                return win

            print(player1)
            print("Зачеркнуть цифру? (y/n)")
            answer = input()
            win = player1.player_turn(number, answer)
        else:
            print(player2)
            print(player1)
            win = player1.computer_turn(number) or player2.computer_turn(number)

        if win:
            if player1.win:
                return f"Выиграл {repr(player1)}"
            elif player2.win:
                return f"Выиграл {repr(player2)}"
            else:
                return win


def main():
    card = Card()
    card1 = Card()
    players_type = input("Выберите тип игроков(1.компьютер - человек, 2.человек - человек, 3.компьютер - компьютер)\n")

    if players_type == "1":
        player_comp = Player(card)
        player = Player(card1, 1, False)
        print(play(player_comp, player, 1))

    elif players_type == "2":
        player1 = Player(card, 1, False)
        player2 = Player(card1, 2, False)
        print(play(player1, player2, 2))

    else:
        player_comp1 = Player(card, 1)
        player_comp2 = Player(card1, 2)
        print(play(player_comp1, player_comp2, 3))


if __name__ == '__main__':
    main()
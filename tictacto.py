from typing import List
from enum import Enum


class FIELD_ELEMENT(Enum):
    EMPTY = 1
    PLAYER_X = 2
    PLAYER_O = 3


def visualize(field: List[List], numerate_empty_slots: bool = True):
    symbol_map = {
        FIELD_ELEMENT.EMPTY: " ",
        FIELD_ELEMENT.PLAYER_X: "x",
        FIELD_ELEMENT.PLAYER_O: "o",
    }
    row_seperator = "\n+-+-+-+\n"
    col_seperator = "|"

    out = row_seperator
    for i_row in range(3):
        out += col_seperator
        for i_col in range(3):
            elem = field[i_row][i_col]
            if elem == FIELD_ELEMENT.EMPTY and numerate_empty_slots:
                out += str(i_row * 3 + i_col + 1)
            else:
                out += symbol_map[elem]
            out += col_seperator
        out += row_seperator

    print(out)


def check_game_over(field: List[List]):
    diagonals = [
        [field[0][0], field[1][1], field[2][2]],
        [field[0][2], field[1][1], field[2][0]],
    ]

    to_check = field + list(zip(*field)) + diagonals

    for possible_strike in to_check:
        if (
            FIELD_ELEMENT.EMPTY not in possible_strike
            and len(set(possible_strike)) == 1
        ):
            return True

    return False


def validate_input(position_input: str, field: List[List]):
    if not position_input.isnumeric():
        print("Wrong input: Please enter only digits!")
        return False

    if not (0 < int(position_input) < 10):
        print("Wrong input: Please enter only numbers from 1-9!")
        return False

    i_row, i_col = divmod(int(position_input) - 1, 3)
    if field[i_row][i_col] != FIELD_ELEMENT.EMPTY:
        print("Wrong input: This field is already occupied.")
        return False

    return True


def gather_input(player_name: str, field: List[List]):
    while True:
        position = input(
            f"Player {player_name}: Please enter the number of the field you want to occupy."
        )
        if validate_input(position, field):
            break

    return divmod(int(position) - 1, 3)


def tictacto():
    # create a empty field
    field = []
    for row in range(3):
        field.append([FIELD_ELEMENT.EMPTY for col in range(3)])

    turn_counter = 0
    while not check_game_over(field):
        current_player = FIELD_ELEMENT.PLAYER_X if turn_counter % 2 else FIELD_ELEMENT.PLAYER_O
        if current_player == FIELD_ELEMENT.PLAYER_X:
            player_name = "X"
        else:
            player_name = "O"

        visualize(field)
        
        i_row, i_col = gather_input(player_name, field)
        field[i_row][i_col] = current_player

        turn_counter += 1
    
    print(f"Player {player_name} wins.")

    visualize(field)


if __name__ == "__main__":
    tictacto()

letters = 'ABCDEFGH'


def to_tuple(cell_string):
    letter = letters.find(cell_string[0]) + 1
    answer = (letter, cell_string[1])
    return answer


def to_string(cell_tuple):
    answer = ''
    answer += str(letters[cell_tuple[0] - 1]) + str(cell_tuple[1])
    return answer


def is_on_table(cell_int):
    first = int(cell_int[0])
    second = int(cell_int[1])
    if 9 > first > 0 and 9 > second > 0:
        return True
    else:
        return False


def possible_turns(cell):
    cell = to_tuple(cell)
    letter = int(cell[0])
    number = int(cell[1])
    turns = []
    prob_turns = [(letter - 2, number - 1), (letter - 2, number + 1), (letter + 2, number - 1),
                  (letter + 2, number + 1), (letter - 1, number - 2), (letter + 1, number - 2),
                  (letter - 1, number + 2), (letter + 1, number + 2)]
    for i in prob_turns:
        if is_on_table(i):
            turns.append(to_string(i))
    turns.sort()
    return turns


print(possible_turns("D4"))
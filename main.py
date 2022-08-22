from random import randint
from copy import deepcopy


board = [["", "", "", ""],
         ["", "", "", ""],
         ["", "", "", ""],
         ["", "", "", ""]]


def print_board():
    print("+---------------------------+")
    for row in board:
        x = "|"
        for col in row:
            x += f"{col:^6}" + "|"
        print(x)
        print("+---------------------------+")


def is_game_over():
    global board
    for row in board:
        for col in row:
            if (col == ""):
                return False

    temp = deepcopy(board)
    combine_left_right_templete(0, 1, 2, 3)
    move_left_right_templete(1, 0, 2, 3)
    if (temp != board):
        board = deepcopy(temp)
        return False
    combine_left_right_templete(3, 2, 1, 0)
    move_left_right_templete(2, 3, 1, 0)
    if (temp != board):
        board = deepcopy(temp)
        return False
    combine_up_down_templete(0, 1, 2, 3)
    move_up_down_templete(1, 0, 2, 3)
    if (temp != board):
        board = deepcopy(temp)
        return False
    move_up_down_templete(2, 3, 1, 0)
    if (temp != board):
        board = deepcopy(temp)
        return False

    return True


def winner():
    for row in board:
        for col in row:
            if col == 2048:
                return True
    return False


def get_rand_tile():
    rand_row = randint(0, 3)
    rand_col = randint(0, 3)

    while (board[rand_row][rand_col] != ""):
        rand_row = randint(0, 3)
        rand_col = randint(0, 3)

    return (rand_row, rand_col)


def move_left_right_templete(w, x, y, z):
    for _ in range(4):
        for i in range(4):
            if (board[i][w] != "" and board[i][x] == ""):
                board[i][x] = board[i][w]
                board[i][w] = ""
            if (board[i][y] != "" and board[i][w] == ""):
                board[i][w] = board[i][y]
                board[i][y] = ""
            if (board[i][z] != "" and board[i][y] == ""):
                board[i][y] = board[i][z]
                board[i][z] = ""


def move_up_down_templete(a, b, c, d):
    for _ in range(4):
        for i in range(4):
            if (board[a][i] != "" and board[b][i] == ""):
                board[b][i] = board[a][i]
                board[a][i] = ""
            if (board[c][i] != "" and board[a][i] == ""):
                board[a][i] = board[c][i]
                board[c][i] = ""
            if (board[d][i] != "" and board[c][i] == ""):
                board[c][i] = board[d][i]
                board[d][i] = ""


def combine_left_right_templete(w, x, y, z):
    for i in range(4):
        if (board[i][w] != ""):
            if (board[i][x] == board[i][w]):
                board[i][x] = ""
                board[i][w] = board[i][w] * 2
            elif ((board[i][x] == "") and (board[i][y] == board[i][w])):
                board[i][y] = ""
                board[i][w] = board[i][w] * 2
            elif ((board[i][x] == "") and (board[i][y] == "") and (board[i][z] == board[i][w])):
                board[i][z] = ""
                board[i][w] = board[i][w] * 2

        if (board[i][x] != ""):
            if (board[i][y] == board[i][x]):
                board[i][y] = ""
                board[i][x] = board[i][x] * 2
            elif ((board[i][y] == "") and (board[i][z] == board[i][x])):
                board[i][z] = ""
                board[i][x] = board[i][x] * 2

        if ((board[i][y] != "") and (board[i][z] == board[i][y])):
            board[i][z] = ""
            board[i][y] = board[i][y] * 2


def combine_up_down_templete(a, b, c, d):
    for i in range(4):
        if (board[a][i] != ""):
            if (board[b][i] == board[a][i]):
                board[b][i] = ""
                board[a][i] = board[a][i] * 2
            elif ((board[b][i] == "") and (board[c][i] == board[a][i])):
                board[c][i] = ""
                board[a][i] = board[a][i] * 2
            elif ((board[b][i] == "") and (board[c][i] == "") and (board[d][i] == board[a][i])):
                board[d][i] = ""
                board[a][i] = board[a][i] * 2

        if (board[b][i] != ""):
            if (board[c][i] == board[b][i]):
                board[c][i] = ""
                board[b][i] = board[b][i] * 2
            elif ((board[c][i] == "") and (board[d][i] == board[b][i])):
                board[d][i] = ""
                board[b][i] = board[b][i] * 2

        if ((board[c][i] != "") and (board[d][i] == board[c][i])):
            board[d][i] = ""
            board[c][i] = board[c][i] * 2


if __name__ == "__main__":
    flag = False

    while (True):
        if (flag == False):
            r = get_rand_tile()
            board[r[0]][r[1]] = 2
        else:
            flag = False

        print_board()

        if(is_game_over()):
            print("Game Over!")
            break

        if (winner()):
            print("You Won!")
            break

        user_input = input()
        while (user_input not in ['a', 'w', 's', 'd', 'Q']):
            user_input = input()

        temp_board = deepcopy(board)

        if (user_input == 'Q'):
            break

        # move left
        elif (user_input == 'a'):
            combine_left_right_templete(0, 1, 2, 3)
            move_left_right_templete(1, 0, 2, 3)

        # move right
        elif (user_input == 'd'):
            combine_left_right_templete(3, 2, 1, 0)
            move_left_right_templete(2, 3, 1, 0)

        # move up
        elif (user_input == 'w'):
            combine_up_down_templete(0, 1, 2, 3)
            move_up_down_templete(1, 0, 2, 3)

        # move down
        else:
            combine_up_down_templete(3, 2, 1, 0)
            move_up_down_templete(2, 3, 1, 0)

        if (board == temp_board):
            flag = True

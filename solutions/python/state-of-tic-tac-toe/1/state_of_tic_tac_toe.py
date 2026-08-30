def gamestate(board):

    x_count = 0
    o_count = 0

    x_won = False
    o_won = False

    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1

    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    for row in board:
        if (row[0], row[1], row[2]) == ("X", "X", "X"):
            x_won = True
        elif (row[0], row[1], row[2]) == ("O", "O", "O"):
            o_won = True

    for column in range(3):
        if board[0][column] == "O" and board[1][column] == "O" and board[2][column] == "O":
            o_won = True
        elif board[0][column] == "X" and board[1][column] == "X" and board[2][column] == "X":
            x_won = True

    if (board[0][0] == "X"
        and board[1][1] == "X"
        and board[2][2] == "X"):
        x_won = True

    if (board[0][2] == "X"
        and board[1][1] == "X"
        and board[2][0] == "X"):
        x_won = True

    if (board[0][0] == "O"
        and board[1][1] == "O"
        and board[2][2] == "O"):
        o_won = True

    if (board[0][2] == "O"
        and board[1][1] == "O"
        and board[2][0] == "O"):
        o_won = True

    if x_won and o_won:
        raise ValueError("Impossible board: game should have ended after the game was won")

    if x_won and x_count != o_count + 1:
        raise ValueError("Wrong turn order: X went twice")

    if o_won and x_count != o_count:
        raise ValueError("Wrong turn order: O started")

    if x_won or o_won:
        return "win"

    for row in board:
        for cell in row:
            if cell == " ":
                return "ongoing"

    return "draw"
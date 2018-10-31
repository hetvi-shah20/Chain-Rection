import board

game_board = board.Board()
while True:
    x, y = input("[Player 1] Enter Values for Row and Column of your move separated by space").split(" ")
    x, y = int(x), int(y)
    move_value = game_board.positive_move(x, y)
    while(move_value == 9):
        print("Entered valued are ocupied by other player")
        x, y = input("[Player 1] Enter Values for Row and Column of your move separated by space").split(" ")
        x, y = int(x), int(y)
        move_value = game_board.positive_move(x, y)

    game_board.positive_expand(x, y)
    print(game_board)
    x, y = input("[Player 2]Enter Values for Row and Column of your move separated by space").split(" ")
    x, y = int(x), int(y)
    move_value = game_board.negative_move(x, y)
    while(move_value==9):
        print("Entered valued are ocupied by other player")
        x, y = input("[Player 2]Enter Values for Row and Column of your move separated by space").split(" ")
        x, y = int(x), int(y)
        move_value = game_board.negative_move(x, y)
    game_board.negative_expand(x, y)
    print(game_board)
    n = input("q for quitting the game")
    if n == "q":
        break

print(game_board)
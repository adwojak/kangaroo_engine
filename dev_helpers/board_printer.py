def printer(element):
    from pprint import pprint
    # Avoiding reference sharing
    board = [["-" for _ in range(8)] for __ in range(8)]
    board[element.vertical_position][element.horizontal_position] = "0"
    for vertical_move, horizontal_move in element.calculate_moves():
        board[vertical_move][horizontal_move] = "m"
    pprint(board)

from Tic_Tac_Toe.tic_tac_toe.board import board_print

brd = {'1': ' ', '2': ' ', '3': ' ',
       '4': ' ', '5': ' ', '6': ' ',
       '7': ' ', '8': ' ', '9': ' '}

board_keys = []

for key in brd:
    board_keys.append(key)


def game():
    turn = 'X'
    count = 0

    for i in range(10):
        board_print(brd)
        print("your turn," + turn + ".move to?")

        move = input()

        if brd[move] == ' ':
            brd[move] = turn
            count += 1
        else:
            print("place is already filled.\nmove to ?")
            continue
        # game functionality
        if count >= 5:
            if brd['7'] == brd['8'] == brd['9'] != ' ':  # the top
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break
            elif brd['4'] == brd['5'] == brd['6'] != ' ':  # the middle
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break
            elif brd['1'] == brd['2'] == brd['3'] != ' ':  # the bottom
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break
            elif brd['1'] == brd['4'] == brd['7'] != ' ':  # left side
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break
            elif brd['2'] == brd['5'] == brd['8'] != ' ':  # middle
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break
            elif brd['3'] == brd['6'] == brd['9'] != ' ':  # right side
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break
            elif brd['7'] == brd['5'] == brd['3'] != ' ':  # diagonal
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break
            elif brd['1'] == brd['5'] == brd['9'] != ' ':  # diagonal
                board_print(brd)
                print("\nGame Over!!.\n")
                print(" **** " + turn + " is Winner!!. ****")
                break

        if count == 9:
            print("\nGame Over!!.\n")
            print("Tie!!")

        # change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # ask if player wants to restart the game or not.
    restart = input("play again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            brd[key] = " "

        game()


if __name__ == "__main__":
    game()
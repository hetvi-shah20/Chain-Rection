from tkinter import *
import board

game_board = board.Board()

root = Tk()
root.minsize(520, 500)
root.geometry("50x20")
root.resizable(0, 0)

frame = Frame(root)


def b00():
    bv00.set("1")
    move_value = game_board.positive_move(0, 0)
    while (move_value == 9):
        print("Entered valued are ocupied by other player")
        x, y = input("[Player 1] Enter Values for Row and Column of your move separated by space").split(" ")
        x, y = int(x), int(y)
        move_value = game_board.positive_move(x, y)
    print(game_board)
    print('grid')


bv00=StringVar()
btn00 = Button(frame, textvariable=bv00, command=b00, height=3, width=6)


def new_game(master):
    global frame
    frame.grid()
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    r5 = []
    r6 = []
    r7 = []
    r8 = []
    r9 = []
    r0 = []
    grid = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r0]

    grid[0].append(btn00)
    grid[0][0].grid(row=0, column=0)
    grid[0].append(Button(frame, text="", command=b01, height=3, width=6))
    grid[0][1].grid(row=0, column=1)
    grid[0].append(Button(frame, text="", command=b02, height=3, width=6))
    grid[0][2].grid(row=0, column=2)
    grid[0].append(Button(frame, text="", command=b03, height=3, width=6))
    grid[0][3].grid(row=0, column=3)
    grid[0].append(Button(frame, text="", command=b04, height=3, width=6))
    grid[0][4].grid(row=0, column=4)
    grid[0].append(Button(frame, text="", command=b05, height=3, width=6))
    grid[0][5].grid(row=0, column=5)
    grid[0].append(Button(frame, text="", command=b06, height=3, width=6))
    grid[0][6].grid(row=0, column=6)
    grid[0].append(Button(frame, text="", command=b07, height=3, width=6))
    grid[0][7].grid(row=0, column=7)
    grid[0].append(Button(frame, text="", command=b08, height=3, width=6))
    grid[0][8].grid(row=0, column=8)
    grid[0].append(Button(frame, text="", command=b09, height=3, width=6))
    grid[0][9].grid(row=0, column=9)
    grid[1].append(Button(frame, text="", command=b10, height=3, width=6))
    grid[1][0].grid(row=1, column=0)
    grid[1].append(Button(frame, text="", command=b11, height=3, width=6))
    grid[1][1].grid(row=1, column=1)
    grid[1].append(Button(frame, text="", command=b12, height=3, width=6))
    grid[1][2].grid(row=1, column=2)
    grid[1].append(Button(frame, text="", command=b13, height=3, width=6))
    grid[1][3].grid(row=1, column=3)
    grid[1].append(Button(frame, text="", command=b14, height=3, width=6))
    grid[1][4].grid(row=1, column=4)
    grid[1].append(Button(frame, text="", command=b15, height=3, width=6))
    grid[1][5].grid(row=1, column=5)
    grid[1].append(Button(frame, text="", command=b16, height=3, width=6))
    grid[1][6].grid(row=1, column=6)
    grid[1].append(Button(frame, text="", command=b17, height=3, width=6))
    grid[1][7].grid(row=1, column=7)
    grid[1].append(Button(frame, text="", command=b18, height=3, width=6))
    grid[1][8].grid(row=1, column=8)
    grid[1].append(Button(frame, text="", command=b19, height=3, width=6))
    grid[1][9].grid(row=1, column=9)
    grid[2].append(Button(frame, text="", command=b20, height=3, width=6))
    grid[2][0].grid(row=2, column=0)
    grid[2].append(Button(frame, text="", command=b21, height=3, width=6))
    grid[2][1].grid(row=2, column=1)
    grid[2].append(Button(frame, text="", command=b22, height=3, width=6))
    grid[2][2].grid(row=2, column=2)
    grid[2].append(Button(frame, text="", command=b23, height=3, width=6))
    grid[2][3].grid(row=2, column=3)
    grid[2].append(Button(frame, text="", command=b24, height=3, width=6))
    grid[2][4].grid(row=2, column=4)
    grid[2].append(Button(frame, text="", command=b25, height=3, width=6))
    grid[2][5].grid(row=2, column=5)
    grid[2].append(Button(frame, text="", command=b26, height=3, width=6))
    grid[2][6].grid(row=2, column=6)
    grid[2].append(Button(frame, text="", command=b27, height=3, width=6))
    grid[2][7].grid(row=2, column=7)
    grid[2].append(Button(frame, text="", command=b28, height=3, width=6))
    grid[2][8].grid(row=2, column=8)
    grid[2].append(Button(frame, text="", command=b29, height=3, width=6))
    grid[2][9].grid(row=2, column=9)
    grid[3].append(Button(frame, text="", command=b30, height=3, width=6))
    grid[3][0].grid(row=3, column=0)
    grid[3].append(Button(frame, text="", command=b31, height=3, width=6))
    grid[3][1].grid(row=3, column=1)
    grid[3].append(Button(frame, text="", command=b32, height=3, width=6))
    grid[3][2].grid(row=3, column=2)
    grid[3].append(Button(frame, text="", command=b33, height=3, width=6))
    grid[3][3].grid(row=3, column=3)
    grid[3].append(Button(frame, text="", command=b34, height=3, width=6))
    grid[3][4].grid(row=3, column=4)
    grid[3].append(Button(frame, text="", command=b35, height=3, width=6))
    grid[3][5].grid(row=3, column=5)
    grid[3].append(Button(frame, text="", command=b36, height=3, width=6))
    grid[3][6].grid(row=3, column=6)
    grid[3].append(Button(frame, text="", command=b37, height=3, width=6))
    grid[3][7].grid(row=3, column=7)
    grid[3].append(Button(frame, text="", command=b38, height=3, width=6))
    grid[3][8].grid(row=3, column=8)
    grid[3].append(Button(frame, text="", command=b39, height=3, width=6))
    grid[3][9].grid(row=3, column=9)
    grid[4].append(Button(frame, text="", command=b40, height=3, width=6))
    grid[4][0].grid(row=4, column=0)
    grid[4].append(Button(frame, text="", command=b41, height=3, width=6))
    grid[4][1].grid(row=4, column=1)
    grid[4].append(Button(frame, text="", command=b42, height=3, width=6))
    grid[4][2].grid(row=4, column=2)
    grid[4].append(Button(frame, text="", command=b43, height=3, width=6))
    grid[4][3].grid(row=4, column=3)
    grid[4].append(Button(frame, text="", command=b44, height=3, width=6))
    grid[4][4].grid(row=4, column=4)
    grid[4].append(Button(frame, text="", command=b45, height=3, width=6))
    grid[4][5].grid(row=4, column=5)
    grid[4].append(Button(frame, text="", command=b46, height=3, width=6))
    grid[4][6].grid(row=4, column=6)
    grid[4].append(Button(frame, text="", command=b47, height=3, width=6))
    grid[4][7].grid(row=4, column=7)
    grid[4].append(Button(frame, text="", command=b48, height=3, width=6))
    grid[4][8].grid(row=4, column=8)
    grid[4].append(Button(frame, text="", command=b49, height=3, width=6))
    grid[4][9].grid(row=4, column=9)
    grid[5].append(Button(frame, text="", command=b50, height=3, width=6))
    grid[5][0].grid(row=5, column=0)
    grid[5].append(Button(frame, text="", command=b51, height=3, width=6))
    grid[5][1].grid(row=5, column=1)
    grid[5].append(Button(frame, text="", command=b52, height=3, width=6))
    grid[5][2].grid(row=5, column=2)
    grid[5].append(Button(frame, text="", command=b53, height=3, width=6))
    grid[5][3].grid(row=5, column=3)
    grid[5].append(Button(frame, text="", command=b54, height=3, width=6))
    grid[5][4].grid(row=5, column=4)
    grid[5].append(Button(frame, text="", command=b55, height=3, width=6))
    grid[5][5].grid(row=5, column=5)
    grid[5].append(Button(frame, text="", command=b56, height=3, width=6))
    grid[5][6].grid(row=5, column=6)
    grid[5].append(Button(frame, text="", command=b57, height=3, width=6))
    grid[5][7].grid(row=5, column=7)
    grid[5].append(Button(frame, text="", command=b58, height=3, width=6))
    grid[5][8].grid(row=5, column=8)
    grid[5].append(Button(frame, text="", command=b59, height=3, width=6))
    grid[5][9].grid(row=5, column=9)
    grid[6].append(Button(frame, text="", command=b60, height=3, width=6))
    grid[6][0].grid(row=6, column=0)
    grid[6].append(Button(frame, text="", command=b61, height=3, width=6))
    grid[6][1].grid(row=6, column=1)
    grid[6].append(Button(frame, text="", command=b62, height=3, width=6))
    grid[6][2].grid(row=6, column=2)
    grid[6].append(Button(frame, text="", command=b63, height=3, width=6))
    grid[6][3].grid(row=6, column=3)
    grid[6].append(Button(frame, text="", command=b64, height=3, width=6))
    grid[6][4].grid(row=6, column=4)
    grid[6].append(Button(frame, text="", command=b65, height=3, width=6))
    grid[6][5].grid(row=6, column=5)
    grid[6].append(Button(frame, text="", command=b66, height=3, width=6))
    grid[6][6].grid(row=6, column=6)
    grid[6].append(Button(frame, text="", command=b67, height=3, width=6))
    grid[6][7].grid(row=6, column=7)
    grid[6].append(Button(frame, text="", command=b68, height=3, width=6))
    grid[6][8].grid(row=6, column=8)
    grid[6].append(Button(frame, text="", command=b69, height=3, width=6))
    grid[6][9].grid(row=6, column=9)
    grid[7].append(Button(frame, text="", command=b70, height=3, width=6))
    grid[7][0].grid(row=7, column=0)
    grid[7].append(Button(frame, text="", command=b71, height=3, width=6))
    grid[7][1].grid(row=7, column=1)
    grid[7].append(Button(frame, text="", command=b72, height=3, width=6))
    grid[7][2].grid(row=7, column=2)
    grid[7].append(Button(frame, text="", command=b73, height=3, width=6))
    grid[7][3].grid(row=7, column=3)
    grid[7].append(Button(frame, text="", command=b74, height=3, width=6))
    grid[7][4].grid(row=7, column=4)
    grid[7].append(Button(frame, text="", command=b75, height=3, width=6))
    grid[7][5].grid(row=7, column=5)
    grid[7].append(Button(frame, text="", command=b76, height=3, width=6))
    grid[7][6].grid(row=7, column=6)
    grid[7].append(Button(frame, text="", command=b77, height=3, width=6))
    grid[7][7].grid(row=7, column=7)
    grid[7].append(Button(frame, text="", command=b78, height=3, width=6))
    grid[7][8].grid(row=7, column=8)
    grid[7].append(Button(frame, text="", command=b79, height=3, width=6))
    grid[7][9].grid(row=7, column=9)
    grid[8].append(Button(frame, text="", command=b80, height=3, width=6))
    grid[8][0].grid(row=8, column=0)
    grid[8].append(Button(frame, text="", command=b81, height=3, width=6))
    grid[8][1].grid(row=8, column=1)
    grid[8].append(Button(frame, text="", command=b82, height=3, width=6))
    grid[8][2].grid(row=8, column=2)
    grid[8].append(Button(frame, text="", command=b83, height=3, width=6))
    grid[8][3].grid(row=8, column=3)
    grid[8].append(Button(frame, text="", command=b84, height=3, width=6))
    grid[8][4].grid(row=8, column=4)
    grid[8].append(Button(frame, text="", command=b85, height=3, width=6))
    grid[8][5].grid(row=8, column=5)
    grid[8].append(Button(frame, text="", command=b86, height=3, width=6))
    grid[8][6].grid(row=8, column=6)
    grid[8].append(Button(frame, text="", command=b87, height=3, width=6))
    grid[8][7].grid(row=8, column=7)
    grid[8].append(Button(frame, text="", command=b88, height=3, width=6))
    grid[8][8].grid(row=8, column=8)
    grid[8].append(Button(frame, text="", command=b89, height=3, width=6))
    grid[8][9].grid(row=8, column=9)
    grid[9].append(Button(frame, text="", command=b90, height=3, width=6))
    grid[9][0].grid(row=9, column=0)
    grid[9].append(Button(frame, text="", command=b91, height=3, width=6))
    grid[9][1].grid(row=9, column=1)
    grid[9].append(Button(frame, text="", command=b92, height=3, width=6))
    grid[9][2].grid(row=9, column=2)
    grid[9].append(Button(frame, text="", command=b93, height=3, width=6))
    grid[9][3].grid(row=9, column=3)
    grid[9].append(Button(frame, text="", command=b94, height=3, width=6))
    grid[9][4].grid(row=9, column=4)
    grid[9].append(Button(frame, text="", command=b95, height=3, width=6))
    grid[9][5].grid(row=9, column=5)
    grid[9].append(Button(frame, text="", command=b96, height=3, width=6))
    grid[9][6].grid(row=9, column=6)
    grid[9].append(Button(frame, text="", command=b97, height=3, width=6))
    grid[9][7].grid(row=9, column=7)
    grid[9].append(Button(frame, text="", command=b98, height=3, width=6))
    grid[9][8].grid(row=9, column=8)
    grid[9].append(Button(frame, text="", command=b99, height=3, width=6))
    grid[9][9].grid(row=9, column=9)
    

def callback():
    print("click!")
    b.destroy()
    new_game(root)

#
# def b00():
#     bv00.set("1")
#     print('grid')


def b01():
    print('grid')


def b02():
    print('grid')


def b03():
    print('grid')


def b04():
    print('grid')


def b05():
    print('grid')


def b06():
    print('grid')


def b07():
    print('grid')


def b08():
    print('grid')


def b09():
    print('grid')


def b10():
    print('grid')


def b11():
    print('grid')


def b12():
    print('grid')


def b13():
    print('grid')


def b14():
    print('grid')


def b15():
    print('grid')


def b16():
    print('grid')


def b17():
    print('grid')


def b18():
    print('grid')


def b19():
    print('grid')


def b20():
    print('grid')


def b21():
    print('grid')


def b22():
    print('grid')


def b23():
    print('grid')


def b24():
    print('grid')


def b25():
    print('grid')


def b26():
    print('grid')


def b27():
    print('grid')


def b28():
    print('grid')


def b29():
    print('grid')


def b30():
    print('grid')


def b31():
    print('grid')


def b32():
    print('grid')


def b33():
    print('grid')


def b34():
    print('grid')


def b35():
    print('grid')


def b36():
    print('grid')


def b37():
    print('grid')


def b38():
    print('grid')


def b39():
    print('grid')


def b40():
    print('grid')


def b41():
    print('grid')


def b42():
    print('grid')


def b43():
    print('grid')


def b44():
    print('grid')


def b45():
    print('grid')


def b46():
    print('grid')


def b47():
    print('grid')


def b48():
    print('grid')


def b49():
    print('grid')


def b50():
    print('grid')


def b51():
    print('grid')


def b52():
    print('grid')


def b53():
    print('grid')


def b54():
    print('grid')


def b55():
    print('grid')


def b56():
    print('grid')


def b57():
    print('grid')


def b58():
    print('grid')


def b59():
    print('grid')


def b60():
    print('grid')


def b61():
    print('grid')


def b62():
    print('grid')


def b63():
    print('grid')


def b64():
    print('grid')


def b65():
    print('grid')


def b66():
    print('grid')


def b67():
    print('grid')


def b68():
    print('grid')


def b69():
    print('grid')


def b70():
    print('grid')


def b71():
    print('grid')


def b72():
    print('grid')


def b73():
    print('grid')


def b74():
    print('grid')


def b75():
    print('grid')


def b76():
    print('grid')


def b77():
    print('grid')


def b78():
    print('grid')


def b79():
    print('grid')


def b80():
    print('grid')


def b81():
    print('grid')


def b82():
    print('grid')


def b83():
    print('grid')


def b84():
    print('grid')


def b85():
    print('grid')


def b86():
    print('grid')


def b87():
    print('grid')


def b88():
    print('grid')


def b89():
    print('grid')


def b90():
    print('grid')


def b91():
    print('grid')


def b92():
    print('grid')


def b93():
    print('grid')


def b94():
    print('grid')


def b95():
    print('grid')


def b96():
    print('grid')


def b97():
    print('grid')


def b98():
    print('grid')


def b99():
    print('grid')


b = Button(root, text="Start Game", command=callback)
b.place(x=275, y=275)


root.mainloop()

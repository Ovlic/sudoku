import turtle
import copy
import random
from turtle import Turtle, Screen
import numpy as np

random.seed(0)

def f_draw_sudoku(a, sp=None):
    row1 = a[0]
    row2 = a[1]
    row3 = a[2]
    row4 = a[3]
    row5 = a[4]
    row6 = a[5]
    row7 = a[6]
    row8 = a[7]
    row9 = a[8]
    draw_sudoku(row1, row2, row3, row4, row5, row6, row7, row8, row9, sp)

def squarify(i, j, row1, row2, row3, row4, row5, row6, row7, row8, row9):
    cc = []
    if i >= 1 and i <= 3:
        # row 1, 2, 3
        if j >= 1 and j <= 3:
            # column 1, 2, 3
            cc = [row1[0], row1[1], row1[2], row2[0], row2[1], row2[2], row3[0], row3[1], row3[2]]
        elif j >= 4 and j <= 6:
            # column 4, 5, 6
            cc = [row1[3], row1[4], row1[5], row2[3], row2[4], row2[5], row3[3], row3[4], row3[5]]
        elif j >= 7 and j <= 9:
            # column 7, 8, 9
            cc = [row1[6], row1[7], row1[8], row2[6], row2[7], row2[8], row3[6], row3[7], row3[8]]
    elif i >= 4 and i <= 6:
        # row 4, 5, 6
        if j >= 1 and j <= 3:
            # column 1, 2, 3
            cc = [row4[0], row4[1], row4[2], row5[0], row5[1], row5[2], row6[0], row6[1], row6[2]]
        elif j >= 4 and j <= 6:
            # column 4, 5, 6
            cc = [row4[3], row4[4], row4[5], row5[3], row5[4], row5[5], row6[3], row6[4], row6[5]]
        elif j >= 7 and j <= 9:
            # column 7, 8, 9
            cc = [row4[6], row4[7], row4[8], row5[6], row5[7], row5[8], row6[6], row6[7], row6[8]]
    elif i >= 7 and i <= 9:
        # row 7, 8, 9
        if j >= 1 and j <= 3:
            # column 1, 2, 3
            cc = [row7[0], row7[1], row7[2], row8[0], row8[1], row8[2], row9[0], row9[1], row9[2]]
        elif j >= 4 and j <= 6:
            # column 4, 5, 6
            cc = [row7[3], row7[4], row7[5], row8[3], row8[4], row8[5], row9[3], row9[4], row9[5]]
        elif j >= 7 and j <= 9:
            # column 7, 8, 9
            cc = [row7[6], row7[7], row7[8], row8[6], row8[7], row8[8], row9[6], row9[7], row9[8]]
    return cc


def draw_sudoku(r1, r2, r3, r4, r5, r6, r7, r8, r9, sp=None):
    screen = Screen()

    turtle.getscreen()
    screen.title("Sudoku")
    turtle.hideturtle()
    TURTLE_SIZE = 20

    def close_():
        print("Closing window...")
        screen.bye()

    # Set up keybinds
    print("Setting up Keybinds...")
    screen.onkey(close_, "Up")
    screen.onkey(close_, "Escape")
    screen.listen()

    if sp == None: dr_sp = screen.numinput("Speed", "Pick Drawing Speed", default=11, minval=1, maxval=11)
    else: dr_sp = sp
    if dr_sp == None: screen.bye()
    print("Drawing Speed = "+str(dr_sp))

    yertle = Turtle(shape="classic", visible=False)
    yertle.penup()
    yertle.speed(dr_sp)
    yertle.pensize(3)
    yertle.goto(-screen.window_width()/2+50, screen.window_height()/2-50)
    yertle.pendown()
    yertle.showturtle()

    write_num = Turtle(shape="classic", visible=False)
    write_num.penup()
    write_num.speed(dr_sp)
    write_num.pensize(3)

    # Create square
    print("Drawing Square...")
    yertle.goto(abs(yertle.xcor()), yertle.ycor())
    yertle.rt(90)
    yertle.goto(yertle.xcor(), yertle.ycor()*-1)
    yertle.rt(90)
    yertle.goto(yertle.xcor()*-1, yertle.ycor())
    yertle.rt(90)
    yertle.goto(yertle.xcor(), abs(yertle.ycor()))
    yertle.hideturtle()
    yertle.penup()

    x_start = -screen.window_width()/2+50
    x_end = screen.window_width()/2-50
    y_start = screen.window_height()/2-50
    y_end = -screen.window_height()/2+50

    # Rows and Columns
    x_pos = (x_end - x_start)/9
    y_pos = (y_start - y_end)/9

    row = Turtle(shape="classic", visible=False)
    column = Turtle(shape="classic", visible=False)
    column.rt(90)

    # Drawing Rows and Columns
    print("Drawing Rows and Columns...")
    for i in range(1, 9):
        row.pensize(1)
        row.penup()
        row.speed(dr_sp)
        row.goto(x_start, y_start-y_pos*i)
        row.pendown()
        # row.speed(6)
        if i == 3 or i == 6:
            row.pensize(3)
        row.showturtle()

        row.goto(x_end, y_start-y_pos*i)
        row.hideturtle()

        column.pensize(1)
        column.penup()
        column.speed(dr_sp)
        column.goto(x_start+x_pos*i, y_start)
        column.pendown()
        #column.speed(6)
        if i == 3 or i == 6:
            column.pensize(3)
        column.showturtle()
        
        column.goto(x_start+x_pos*i, y_end)
        column.hideturtle()

    # Write Numbers
    print("Writing Numbers...")
    rows_ = [r1, r2, r3, r4, r5, r6, r7, r8, r9]

    def sudoku_write_nums(row1, row2, row3, row4, row5, row6, row7, row8, row9, redraw=False):
        if redraw == True:
            write_num.undo()
        r_ = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
        for i in range(0, 9):
            for j in range(0, 9):
                if r_[i][j] == 0: num = " "
                else: num = r_[i][j]
                if isinstance(r_[i][j], list) == True:
                    print("isinstance = true")
                    write_num.goto(x_start+((x_pos*j)+(x_pos/4)), y_start-(y_pos*i)-(y_pos/4))
                    write_num.write(num, True, align="center", font=("Verdana", 15, "normal"))
                else:
                    write_num.goto(x_start+((x_pos*j)+(x_pos/2)), y_start-((y_pos*i)+(y_pos/2))-25)
                    write_num.write(num, True, align="center", font=("Verdana", 40, "normal"))
    
    sudoku_write_nums(r1, r2, r3, r4, r5, r6, r7, r8, r9)


    print("Done")
    print("Press the \"Escape\" key to exit.")

    arr = []
    for i in range(0, 9):
        # Make an list that has 9 items and in each item it contains 2 sub-lists, one for the min x-cor and max x-cor and one for min y-cor and max y-cor
        x_arr = []
        y_arr = []

        x_arr.append(x_start+(x_pos*i))
        x_arr.append(x_start+(x_pos*(i+1)))

        y_arr.append(y_start-(y_pos*(i+1)))
        y_arr.append(y_start-(y_pos*i))
        
        arr.append([x_arr, y_arr])
    #print(arr)

    def clicked_(cx, cy):
        print("clicked at "+str(cx)+", "+str(cy))
        is_column = False
        is_row = False
        clicked_column = None
        clicked_row = None
        for i in range(0, 9):
            if cx >= arr[i][0][0] and cx <= arr[i][0][1]:
                is_column = True
                clicked_column = i
                print("You clicked column "+str(i+1))
                break
        for i in range(0, 9):
            if cy >= arr[i][1][0] and cy <= arr[i][1][1]:
                is_row = True
                clicked_row = i
                print("You clicked row "+str(i+1))
                break
        
        if is_column == True and is_row == True:
            input_num = int(screen.numinput("Input", "Please enter value for box", minval=1, maxval=9))
            print(input_num)
            print(r9)
            if isinstance(input_num, int) == True:
                rows_[clicked_row][clicked_column] = input_num
                #write_num.clearstamps()
                #write_num.goto(x_start+((x_pos*clicked_column)+(x_pos/2)), y_start-((y_pos*clicked_row)+(y_pos/2))-25)
                #write_num.write(input_num, True, align="center", font=("Verdana", 40, "normal"))
                sudoku_write_nums(r1, r2, r3, r4, r5, r6, r7, r8, r9, redraw=True)
        

    screen.onscreenclick(clicked_, 1)
    screen.listen()

    turtle.mainloop()

def f_s_board(a, sp=None):
    row1 = a[0]
    row2 = a[1]
    row3 = a[2]
    row4 = a[3]
    row5 = a[4]
    row6 = a[5]
    row7 = a[6]
    row8 = a[7]
    row9 = a[8]
    return draw_sudoku(row1, row2, row3, row4, row5, row6, row7, row8, row9, sp)


#solver = solve([0,3,0,4,0,0,1,0,0],[0,0,0,0,1,8,0,0,0],[6,0,0,0,0,3,0,0,0],[0,0,0,0,0,9,0,0,0],[0,8,0,5,3,0,0,7,2],[0,0,0,0,0,0,0,4,0],[0,0,3,9,0,0,4,0,0],[0,2,4,0,0,0,0,6,0],[0,0,5,0,7,0,9,0,0],11)#solve([0, 5, 3, 1, 6, 7, 4, 2, 8],[4, 2, 8, 3, 0, 9, 7, 6, 1],[7, 6, 1, 8, 2, 4, 9, 0, 3],[0, 8, 4, 9, 3, 6, 2, 1, 7],[6, 3, 9, 7, 1, 2, 5, 0, 4],[2, 0, 7, 0, 8, 0, 6, 3, 0],[3, 4, 0, 6, 9, 1, 8, 7, 2],[8, 7, 2, 0, 4, 3, 1, 0, 6],[1, 9, 6, 2, 0, 8, 3, 0, 5])
#print("Finished solving after "+str(solver[9])+" iterations")
#draw_sudoku([0, 5, 3, 1, 6, 7, 4, 2, 8],[4, 2, 8, 3, 0, 9, 7, 6, 1],[7, 6, 1, 8, 2, 4, 9, 0, 3],[0, 8, 4, 9, 3, 6, 2, 1, 7],[6, 3, 9, 7, 1, 2, 5, 0, 4],[2, 0, 7, 0, 8, 0, 6, 3, 0],[3, 4, 0, 6, 9, 1, 8, 7, 2],[8, 7, 2, 0, 4, 3, 1, 0, 6],[1, 9, 6, 2, 0, 8, 3, 0, 5], 11)

def isValid(r, i, n, board):
    #check row
    for k in range(9):
        if board[r][k] == n: # If number is in column
            return False 
    #check column
    for k in range(9):
        if board[k][i] == n:
            return False
    
    #check block
    startrow = r - r % 3 #Get what block its in horizontally (rounds to 0, 3, 6)
    startcol = i- i % 3 #Get what block its in vertically (rounds to 0, 3, 6)
    
    p = startrow

    #  get all numbers in block and check if the number is in it
    while p <= (startrow+2):
        l = startcol
        while l <= (startcol+2):
            if board[p][l] == n:
                return False
            l += 1
        p += 1
    
    return True


def solveSudokuHelper(r, j, board, values):
    if r == 8 and j == 8: #last row, last num
        if board[r][j] != 0: #If the number doesnt equal 0
            for row in board:
                for num in row:
                    values.append(num)
                    #print(num, end=" ")
                #print()
        else: # If the number equals 0
            for n in range(1,10): #1-9
                if isValid(r,j,n,board) == True: # If number can be placed in position
                    board[r][j] = n # Set the number to the correct number
                    for row in board:
                        for num in row:
                            values.append(num)
                            #print(num, end=" ")
                        #print()
                    board[r][j] = 0 # set back to 0 to look for different solutions
        #print()
        return
    
    if j > 8: # If last number in row
        solveSudokuHelper(r+1, 0, board, values) # Call again for next row  
        return
    
    if board[r][j] == 0: 
        for n in range(1,10):
            if isValid(r, j, n, board) == True:
                board[r][j] = n
                solveSudokuHelper(r, j+1, board, values) 
                board[r][j] = 0 # Back to 0 to look for different solutions
    else:
        solveSudokuHelper(r, j+1, board, values) #Call again for next number in row
    return

def solveSudoku(board):
    global values 
    values = []
    solveSudokuHelper(0, 0, board, values)
    #print(len(values))
    if len(values) == 81:
        # print("81!")
        # A complete sudoku board
        res = list(np.array_split(values, 9))
        return True, [list(res[0]), list(res[1]), list(res[2]), list(res[3]), list(res[4]), list(res[5]), list(res[6]), list(res[7]), list(res[8])]

    elif len(values) > 81: return False, []

def remove_numbers(r):
    cant_remove = [] # List of ii jj that cant be removed
    remove_ = True
    rows_count = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    to_be_picked = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]

    while remove_ == True:
        
        change_num = False
        ii = random.choice(rows_count)        
        jj = random.randrange(0, 9)

        
        if jj not in to_be_picked[ii]:
            # Change number by picking from the same row
            print(ii)
            print(to_be_picked[ii])
            jj = random.choice(to_be_picked[ii])


        if r[ii][jj] == 0:
            print("Number picked was 0...")
            change_num = True
        
        for g in range(0, len(cant_remove)):
            if ii == cant_remove[g][0] and jj == cant_remove[g][1]:
                print("Number picked was in unremovable list...")
                change_num = True
        
        if change_num == True:
            print("Changing Number...")
            continue
        num = copy.deepcopy(r[ii][jj])
        to_be_picked[ii].remove(jj)

        if len(to_be_picked[ii]) == 0:
            rows_count.remove(ii)

        r[ii][jj] = 0
        print("Checking solutions...")
        check = solveSudoku(r)
        if check[0] == False:
            print(str(int(len(values)/81))+" solutions found...")
            r[ii][jj] = num
            print("Adding unremovable number to list of unremovable numbers")
            cant_remove.append([ii, jj])
        else: print("Single solution found...")

        not_zero_count = 0
        for g in range(0, 9):
            for h in range(0, 9):
                if r[g][h] != 0: not_zero_count += 1

        if not_zero_count == 24 or len(cant_remove) == not_zero_count: 
            remove_ = False
            return r
        print("Zeros: "+str(not_zero_count))



#thefunction = (solveSudoku([[2, 9, 5, 7, 4, 3, 8, 6, 1],[4, 3, 1, 8, 6, 5, 9, 0, 0],[8, 7, 6, 1, 9, 2, 5, 4, 3],[3, 8, 7, 4, 5, 9, 2, 1, 6],[6, 1, 2, 3, 8, 7, 4, 9, 5],[5, 4, 9, 2, 1, 6, 7, 3, 8],[7, 6, 3, 5, 2, 4, 1, 8, 9],[9, 2, 8, 6, 7, 1, 3, 5, 4],[1, 5, 4, 9, 3, 8, 6, 0, 0]]))#[[0,3,0,4,0,0,1,0,0],[0,0,0,0,1,8,0,0,0],[6,0,0,0,0,3,0,0,0],[0,0,0,0,0,9,0,0,0],[0,8,0,5,3,0,0,7,2],[0,0,0,0,0,0,0,4,0],[0,0,3,9,0,0,4,0,0],[0,2,4,0,0,0,0,6,0],[0,0,5,0,7,0,9,0,0]])
thefunction = (solveSudoku([[0,3,0,4,0,0,1,0,0],[0,0,0,0,1,8,0,0,0],[6,0,0,0,0,3,0,0,0],[0,0,0,0,0,9,0,0,0],[0,8,0,5,3,0,0,7,2],[0,0,0,0,0,0,0,4,0],[0,0,3,9,0,0,4,0,0],[0,2,4,0,0,0,0,6,0],[0,0,5,0,7,0,9,0,0]]))
print(thefunction)




re = remove_numbers(list(thefunction[1]))
f_draw_sudoku(re, 11)


#[[2, 9, 5, 7, 4, 3, 8, 6, 1],[4, 3, 1, 8, 6, 5, 9, 0, 0],[8, 7, 6, 1, 9, 2, 5, 4, 3],[3, 8, 7, 4, 5, 9, 2, 1, 6],[6, 1, 2, 3, 8, 7, 4, 9, 5],[5, 4, 9, 2, 1, 6, 7, 3, 8],[7, 6, 3, 5, 2, 4, 1, 8, 9],[9, 2, 8, 6, 7, 1, 3, 5, 4],[1, 5, 4, 9, 3, 8, 6, 0, 0]]

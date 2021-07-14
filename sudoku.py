import random, collections, turtle
from turtle import Turtle, Screen
import tkinter
from tkinter import filedialog
import os
import copy
import numpy as np
screen = Screen()
screen.setup(width=.50, height=.75, startx=None, starty=None)
screen.title("Sudoku")


# Color console
class color:
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[33m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    reset = '\u001b[0m'
    black_b = '\u001b[40m'
    red_b = '\u001b[41m'
    green_b = '\u001b[42m'
    yellow_b = '\u001b[43m'
    blue_b = '\u001b[44m'
    magenta_b = '\u001b[45m'
    cyan_b = '\u001b[46m'
    white_b = '\u001b[47m'

# Custom Error
class Error(Exception):
    """Base class for other exceptions"""
    pass

class SudokuError(Error):
    """Raised when there is an error with the Sudoku"""

    def __init__(self, rownum, row, message="Match Found"):
        self.rownum = rownum
        self.row = row
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}: {self.rownum}, {self.row}'

# Functions
def split_nums(string):
    nums = []
    for a in string:
        if (a.isnumeric()) == True:
            nums.append(int(a))
    return nums

def close_():
    print("Closing window...")
    screen.bye()

def diff(re):
    root = tkinter
    screen = Screen()
    turtle.hideturtle()
    diff_tle = Turtle(shape="classic", visible=False)
    diff_tle.speed(11)
    
    def close_():
        print("Closing window...")
        screen.bye()
        root.destroy()
        exit("Quit")
        return "quit"
    
    def exec_pz(d):
        screen.reset()
        turtle.hideturtle()
        diff_tle.reset()
        diff_tle.hideturtle()
        
        if isinstance(d, list) == True: f_draw_sudoku(d, 11)
        else:
            remov_ = remove_numbers(list(re), d)
            f_draw_sudoku(remov_, 11)
        return "Quit"
    
    def clicked_(cx, cy):
        #print("x: "+str(cx)+" y: "+str(cy))
        if cx >= -200 and cx <= 200:
            #print("In a box!")
            if cy > -200 and cy < -100:
                print("Extra Hard!")
                print("Not implemented yet.")
                #exec_pz(3)
            elif cy > -100 and cy < 0:
                print("Hard!")
                print("Not implemented yet.")
                #exec_pz(2)
            elif cy > 0 and cy < 100:
                print("Medium")
                exec_pz(1)
            elif cy > 100 and cy < 200:
                print("Easy")
                exec_pz(0)
            elif cy > -500 and cy < -400:
                print("Import")
                
                root = tkinter.Tk()
                root.withdraw() #use to hide tkinter window

                def search_for_file_path ():
                    currdir = os.getcwd()
                    tempdir = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please select a sudoku file', filetypes=[("Sudoku Files", "*.sudoku")])
                    print(tempdir)
                    return tempdir


                file_path_ = search_for_file_path()
                f = open(file_path_.name)
                pz = f.read()
                print(pz)
                print(len(pz))
                print(pz[2:3])
                pz_nums = split_nums(pz)
                r = list(np.array_split(pz_nums, 9))
                exec_pz(r)
                
    turtle.getscreen()
    screen.title("Set Difficulty")
    #diff_tle.hideturtle()

    # Set up keybinds
    print("Setting up Keybinds...")
    screen.onkey(close_, "Up")
    screen.onkey(close_, "Escape")
    screen.listen()

    diff_tle.penup()
    diff_tle.right(90)
    diff_tle.goto(200, 200)
    diff_types = ["Easy", "Medium", "Coming Soon", "Coming Soon"]
    j = -1

    for i in range(200, -200, -100):
        j += 1
        diff_level = diff_types[j]
        diff_tle.penup()
        diff_tle.pendown()
        diff_tle.setx(-200)
        diff_tle.sety(i-100)
        diff_tle.setx(200)
        diff_tle.sety(i)
        diff_tle.setx(-100)
        diff_tle.penup()
        diff_tle.setx(0)
        diff_tle.sety(i-75)
        diff_tle.write(diff_level, False, align="center", font=("Verdana", 35, "normal"))
        diff_tle.sety(i)
    
    diff_tle.penup()
    diff_tle.sety(-300)
    diff_tle.write("(Hard and extra-hard require different code to hide the numbers)", False, align="center", font=("Verdana", 20, "normal"))
    diff_tle.sety(-400)
    diff_tle.pendown()
    diff_tle.setx(-200)
    diff_tle.sety(-500)
    diff_tle.setx(200)
    diff_tle.sety(-400)
    diff_tle.setx(-100)
    diff_tle.penup()
    diff_tle.setx(0)
    diff_tle.sety(-400-75)
    diff_tle.write("Import From File", False, align="center", font=("Verdana", 35, "normal"))

    screen.onscreenclick(clicked_, 1)
    print("Done")
    turtle.mainloop()


def draw_sudoku(r1, r2, r3, r4, r5, r6, r7, r8, r9, sp=None):
    global ans_
    global usr_n
    screen = Screen()

    turtle.getscreen()
    screen.title("Sudoku")
    turtle.hideturtle()
    print(screen.screensize())

    def close_():
        print("Closing window...")
        screen.bye()
        return "Quit"

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

    # Drawing "Save" btn
    yertle.goto(-590, -490)
    yertle.fillcolor("black")
    yertle.pencolor("black")
    yertle.begin_fill()
    yertle.pendown()
    yertle.sety(-530)
    yertle.setx(-330)
    yertle.sety(-490)

    yertle.penup()
    yertle.end_fill()
    yertle.goto(-459.5, -525)
    yertle.pencolor("white")
    yertle.write("Save", False, align="center", font=("Verdana", 20, "normal"))

    # Drawing "show answer" btn
    yertle.goto(330, -490)
    yertle.fillcolor("black")
    yertle.pencolor("black")
    yertle.begin_fill()
    yertle.pendown()
    yertle.sety(-530)
    yertle.setx(590)
    yertle.sety(-490)

    yertle.penup()
    yertle.end_fill()
    yertle.goto(459.5, -525)
    yertle.pencolor("white")
    yertle.write("Solve", False, align="center", font=("Verdana", 20, "normal"))
           


    #cx > -591 and cx < -330 and cy > -530 and cy < -490

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

    ans_ = 0
    usr_n = []

    def clicked_(cx, cy):
        #print("clicked at "+str(cx)+", "+str(cy))
        is_column = False
        is_row = False
        clicked_save_btn = False
        reveal_answer = False
        clicked_column = None
        clicked_row = None
        for i in range(0, 9):
            if cx >= arr[i][0][0] and cx <= arr[i][0][1]:
                is_column = True
                clicked_column = i
                #print("You clicked column "+str(i+1))
                break
        for i in range(0, 9):
            if cy >= arr[i][1][0] and cy <= arr[i][1][1]:
                is_row = True
                clicked_row = i
                #print("You clicked row "+str(i+1))
                break
        if cx > -591 and cx < -330 and cy > -530 and cy < -490:
            #print("Clicked save btn")
            clicked_save_btn = True

        if cx < 591 and cx > 330 and cy > -530 and cy < -490:
            #print("clicked reveal answer")
            reveal_answer = True
        
        if is_column == True and is_row == True or clicked_save_btn == True or reveal_answer == True:
            if clicked_save_btn == False and reveal_answer == False:
                input_num = screen.numinput("Input", "Please enter value for box", minval=1, maxval=9)
                if input_num == None: return
                input_num = int(input_num)
                #print(input_num)
                if isinstance(input_num, int) == True:
                    rows_[clicked_row][clicked_column] = input_num
                    #write_num.clearstamps()
                    #write_num.goto(x_start+((x_pos*clicked_column)+(x_pos/2)), y_start-((y_pos*clicked_row)+(y_pos/2))-25)
                    #write_num.write(input_num, True, align="center", font=("Verdana", 40, "normal"))
                    sudoku_write_nums(r1, r2, r3, r4, r5, r6, r7, r8, r9, redraw=True)
            elif clicked_save_btn == True:
                # Save puzzle
                currdir = os.getcwd()
                root = tkinter.Tk()
                root.withdraw()
                directory = filedialog.asksaveasfilename(parent=root, initialdir=currdir, title='Save As', filetypes=[("Sudoku Files", "*.sudoku")], defaultextension=".sudoku")
                if directory == '': return
                f = open(directory, "w")
                f.write(str([r1, r2, r3, r4, r5, r6, r7, r8, r9]))
                f.close()
            elif reveal_answer == True:
                global ans_
                global usr_n
                ans_ += 1
                if (ans_ % 2) == 0:
                    btn_txt = "Solve"
                    for w in range(0, (81*2)):
                        write_num.undo()
                    #sudoku_write_nums(usr_n[0], usr_n[1], usr_n[2], usr_n[3], usr_n[4], usr_n[5], usr_n[6], usr_n[7], usr_n[8])
                else:
                    r___ = [copy.deepcopy(r1), copy.deepcopy(r2), copy.deepcopy(r3), copy.deepcopy(r4), copy.deepcopy(r5), copy.deepcopy(r6), copy.deepcopy(r7), copy.deepcopy(r8), copy.deepcopy(r9)]
                    for q in range(0, 9):
                        usr_n.append(r___[q])
                    btn_txt = "Hide Answer"
                    ss = solveSudoku([r1, r2, r3, r4, r5, r6, r7, r8, r9])
                    sudoku_write_nums(ss[1][0], ss[1][1], ss[1][2], ss[1][3], ss[1][4], ss[1][5], ss[1][6], ss[1][7], ss[1][8])
                yertle.undo()
                yertle.write(btn_txt, False, align="center", font=("Verdana", 20, "normal"))
        screen.listen()
        

    screen.onscreenclick(clicked_, 1)
    screen.listen()

    turtle.mainloop()

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

def remove_numbers(r, diff):
    cant_remove = [] # List of ii jj that cant be removed
    remove_ = True
    rows_count = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    to_be_picked = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
    
    print(diff)
    if diff == 0:
        # Easy
        set_dif = 28
        #print("28 Numbers expected")
    elif diff == 1:
        # Medium
        set_dif = 25
        #print("25 Numbers expected")
    elif diff == 2:
        # Hard
        set_dif = 22
        #print("22 Numbers expected")
    elif diff == 3:
        set_dif = 17
        #print("17 Numbers expected")

    while remove_ == True:
        
        change_num = False
        try:
            ii = random.choice(rows_count)
        except:
            print("Cant remove:")
            print(len(cant_remove))
        #print(rows_count)
        print(to_be_picked)
        jj = random.randrange(0, 9)

        
        if jj not in to_be_picked[ii]:
            # Change number by picking from the same row
            jj = random.choice(to_be_picked[ii])


        if r[ii][jj] == 0:
            # print("Number picked was 0...")
            change_num = True
        
        for g in range(0, len(cant_remove)):
            if ii == cant_remove[g][0] and jj == cant_remove[g][1]:
                # print("Number picked was in unremovable list...")
                change_num = True
        
        if change_num == True:
            # print("Changing Number...")
            continue
        num = copy.deepcopy(r[ii][jj])
        to_be_picked[ii].remove(jj)

        if len(to_be_picked[ii]) == 0:
            rows_count.remove(ii)

        r[ii][jj] = 0
        # print("Checking solutions...")
        check = solveSudoku(r)
        if check[0] == False:
            # print(str(int(len(values)/81))+" solutions found...")
            r[ii][jj] = num
            # print("Adding unremovable number to list of unremovable numbers")
            cant_remove.append([ii, jj])
        # else: print("Single solution found...")

        not_zero_count = 0
        still_need_to_be_picked = 0
        for g in range(0, 9):
            for h in range(0, 9):
                if r[g][h] != 0: not_zero_count += 1

        for g in range(0, len(to_be_picked)):
            still_need_to_be_picked += len(to_be_picked[g])

        if not_zero_count == set_dif:# or len(cant_remove) == not_zero_count:
            print("Zeros: "+str(not_zero_count))
            print(len(cant_remove))
            print("Expected numbers: "+str(set_dif))
            remove_ = False
            return r
        print("Zeros: "+str(not_zero_count))

def def_r(r):
    if r == 0: return "row1"
    if r == 1: return "row2"
    if r == 2: return "row3"
    if r == 3: return "row4"
    if r == 4: return "row5"
    if r == 5: return "row6"
    if r == 6: return "row7"
    if r == 7: return "row8"
    if r == 8: return "row9"

def print_res(e):
    print("---------------------------")
    for i in range(0, len(e)):
        print("[", end="")
        for j in range(0, 9):
            if j == 8: print(u""+str(e[i][j])+"]")
            else: print(u""+str(e[i][j])+", ", end="")
    print("---------------------------")

def percent(n, r):
    return (n/r)*100

def ft_check(a):
    row1 = a[0]
    row2 = a[1]
    row3 = a[2]
    row4 = a[3]
    row5 = a[4]
    row6 = a[5]
    row7 = a[6]
    row8 = a[7]
    row9 = a[8]
    t_check(row1, row2, row3, row4, row5, row6, row7, row8, row9)
    return

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

def t_rcheck(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    r = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
    for h in range(0, 9):
        for n in range(1, 10):
            # numbers bewteen 1 - 9 in sudoku
            # 9 rows to check for
            c = 0
            for j in range(0, 9):
                # 9 items in row to check for
                if n == r[h][j]:
                    c += 1
                if c >= 2:
                    # i is in the current row at least twice
                    r[h][j] = "**"+str(r[h][j])+"**"
                    return (False, [h, r[h]])
    return (True, [])

def t_check(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    shuffle = (row1, row2, row3, row4, row5, row6, row7, row8, row9)
    r = t_rcheck(row1, row2, row3, row4, row5, row6, row7, row8, row9)
    if r[0] == False:
        e = def_r(r[1][0])
        #print("check: ", False, e, r[1][1])
        raise SudokuError(e, r[1][1])
        #return False, e, r[1][1]
    col1 = [shuffle[0][0], shuffle[1][0], shuffle[2][0], shuffle[3][0], shuffle[4][0], shuffle[5][0], shuffle[6][0], shuffle[7][0], shuffle[8][0]]
    col2 = [shuffle[0][1], shuffle[1][1], shuffle[2][1], shuffle[3][1], shuffle[4][1], shuffle[5][1], shuffle[6][1], shuffle[7][1], shuffle[8][1]]
    col3 = [shuffle[0][2], shuffle[1][2], shuffle[2][2], shuffle[3][2], shuffle[4][2], shuffle[5][2], shuffle[6][2], shuffle[7][2], shuffle[8][2]]
    col4 = [shuffle[0][3], shuffle[1][3], shuffle[2][3], shuffle[3][3], shuffle[4][3], shuffle[5][3], shuffle[6][3], shuffle[7][3], shuffle[8][3]]
    col5 = [shuffle[0][4], shuffle[1][4], shuffle[2][4], shuffle[3][4], shuffle[4][4], shuffle[5][4], shuffle[6][4], shuffle[7][4], shuffle[8][4]]
    col6 = [shuffle[0][5], shuffle[1][5], shuffle[2][5], shuffle[3][5], shuffle[4][5], shuffle[5][5], shuffle[6][5], shuffle[7][5], shuffle[8][5]]
    col7 = [shuffle[0][6], shuffle[1][6], shuffle[2][6], shuffle[3][6], shuffle[4][6], shuffle[5][6], shuffle[6][6], shuffle[7][6], shuffle[8][6]]
    col8 = [shuffle[0][7], shuffle[1][7], shuffle[2][7], shuffle[3][7], shuffle[4][7], shuffle[5][7], shuffle[6][7], shuffle[7][7], shuffle[8][7]]
    col9 = [shuffle[0][8], shuffle[1][8], shuffle[2][8], shuffle[3][8], shuffle[4][8], shuffle[5][8], shuffle[6][8], shuffle[7][8], shuffle[8][8]]
    c = t_rcheck(col1, col2, col3, col4, col5, col6, col7, col8, col9)
    if c[0] == False:
        e = def_r(c[1][0])
        raise SudokuError(e, c[1][1])
        #print("check: ", False, e, c[1][1])
        #return False, e, c[1][1]
    # print("check: ", True)
    return True, []

def test_rows():
    return random.sample(range(1, 10), 9)

def test_sl(arr, sn):
    a_list = collections.deque(arr)
    a_list.rotate(sn)
    shifted_list = list(a_list)
    return shifted_list

def c(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    col1 = [row1[0], row2[0], row3[0], row4[0], row5[0], row6[0], row7[0], row8[0], row9[0]]
    col2 = [row1[1], row2[1], row3[1], row4[1], row5[1], row6[1], row7[1], row8[1], row9[1]]
    col3 = [row1[2], row2[2], row3[2], row4[2], row5[2], row6[2], row7[2], row8[2], row9[2]]
    col4 = [row1[3], row2[3], row3[3], row4[3], row5[3], row6[3], row7[3], row8[3], row9[3]]
    col5 = [row1[4], row2[4], row3[4], row4[4], row5[4], row6[4], row7[4], row8[4], row9[4]]
    col6 = [row1[5], row2[5], row3[5], row4[5], row5[5], row6[5], row7[5], row8[5], row9[5]]
    col7 = [row1[6], row2[6], row3[6], row4[6], row5[6], row6[6], row7[6], row8[6], row9[6]]
    col8 = [row1[7], row2[7], row3[7], row4[7], row5[7], row6[7], row7[7], row8[7], row9[7]]
    col9 = [row1[8], row2[8], row3[8], row4[8], row5[8], row6[8], row7[8], row8[8], row9[8]]

    return col1, col2, col3, col4, col5, col6, col7, col8, col9

def testshuffle(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    for i in range(0, 3):
        if i == 0: r = [row1, row2, row3]
        if i == 1: r = [row4, row5, row6]
        if i == 2: r = [row7, row8, row9]

        ## remove a random row [0-2
        ## save the removed row in p_r3
        pn_r3 = random.randrange(len(r))
        p_r3 = r[pn_r3]
        r.pop(pn_r3)

        ## Remove another row
        ## save the removed row in p_r2
        pn_r2 = random.randrange(len(r))
        p_r2 = r[pn_r2]
        r.pop(pn_r2)

        ## only one row left r[0], save in p_r1
        p_r1 = r[0]

        if i == 0:
            r1 = p_r3
            r2 = p_r2
            r3 = p_r1
        if i == 1:
            r4 = p_r3
            r5 = p_r2
            r6 = p_r1
        if i == 2:
            r7 = p_r3
            r8 = p_r2
            r9 = p_r1
    t_check(r1, r2, r3, r4, r5, r6, r7,r8, r9)
    return r1, r2, r3, r4, r5, r6, r7, r8, r9

def checkmix(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    x = (row1, row2, row3, row4, row5, row6, row7, row8, row9)
    for i in range(0, 21):
        s = testshuffle(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8])
        v = t_check(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])
        # print(s)
        # print(v)
        if v[0] == False:
            # print(False)
            return False, v[1]
        x = c(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])
        # print("-------")
        # print(x)
    return True

def test_rV(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    r1 = [row9[8], row9[7], row9[6], row9[5], row9[4], row9[3], row9[2], row9[1], row9[0]]
    r2 = [row8[8], row8[7], row8[6], row8[5], row8[4], row8[3], row8[2], row8[1], row8[0]]
    r3 = [row7[8], row7[7], row7[6], row7[5], row7[4], row7[3], row7[2], row7[1], row7[0]]
    r4 = [row6[8], row6[7], row6[6], row6[5], row6[4], row6[3], row6[2], row6[1], row6[0]]
    r5 = [row5[8], row5[7], row5[6], row5[5], row5[4], row5[3], row5[2], row5[1], row5[0]]
    r6 = [row4[8], row4[7], row4[6], row4[5], row4[4], row4[3], row4[2], row4[1], row4[0]]
    r7 = [row3[8], row3[7], row3[6], row3[5], row3[4], row3[3], row3[2], row3[1], row3[0]]
    r8 = [row2[8], row2[7], row2[6], row2[5], row2[4], row2[3], row2[2], row2[1], row2[0]]
    r9 = [row1[8], row1[7], row1[6], row1[5], row1[4], row1[3], row1[2], row1[1], row1[0]]

    t_check(r1, r2, r3, r4, r5, r6, r7, r8, r9)
    return r1, r2, r3, r4, r5, r6, r7, r8, r9

def test_rR(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    r1 = [row9[0], row8[0], row7[0], row6[0], row5[0], row4[0], row3[0], row2[0], row1[0]]
    r2 = [row9[1], row8[1], row7[1], row6[1], row5[1], row4[1], row3[1], row2[1], row1[1]]
    r3 = [row9[2], row8[2], row7[2], row6[2], row5[2], row4[2], row3[2], row2[2], row1[2]]
    r4 = [row9[3], row8[3], row7[3], row6[3], row5[3], row4[3], row3[3], row2[3], row1[3]]
    r5 = [row9[4], row8[4], row7[4], row6[4], row5[4], row4[4], row3[4], row2[4], row1[4]]
    r6 = [row9[5], row8[5], row7[5], row6[5], row5[5], row4[5], row3[5], row2[5], row1[5]]
    r7 = [row9[6], row8[6], row7[6], row6[6], row5[6], row4[6], row3[6], row2[6], row1[6]]
    r8 = [row9[7], row8[7], row7[7], row6[7], row5[7], row4[7], row3[7], row2[7], row1[7]]
    r9 = [row9[8], row8[8], row7[8], row6[8], row5[8], row4[8], row3[8], row2[8], row1[8]]

    t_check(r1, r2, r3, r4, r5, r6, r7,r8, r9)
    return r1, r2, r3, r4, r5, r6, r7, r8, r9

def test_rL(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    r1 = [row1[8], row2[8], row3[8], row4[8], row5[8], row6[8], row7[8], row8[8], row9[8]]
    r2 = [row1[7], row2[7], row3[7], row4[7], row5[7], row6[7], row7[7], row8[7], row9[7]]
    r3 = [row1[6], row2[6], row3[6], row4[6], row5[6], row6[6], row7[6], row8[6], row9[6]]
    r4 = [row1[5], row2[5], row3[5], row4[5], row5[5], row6[5], row7[5], row8[5], row9[5]]
    r5 = [row1[4], row2[4], row3[4], row4[4], row5[4], row6[4], row7[4], row8[4], row9[4]]
    r6 = [row1[3], row2[3], row3[3], row4[3], row5[3], row6[3], row7[3], row8[3], row9[3]]
    r7 = [row1[2], row2[2], row3[2], row4[2], row5[2], row6[2], row7[2], row8[2], row9[2]]
    r8 = [row1[1], row2[1], row3[1], row4[1], row5[1], row6[1], row7[1], row8[1], row9[1]]
    r9 = [row1[0], row2[0], row3[0], row4[0], row5[0], row6[0], row7[0], row8[0], row9[0]]
    t_check(r1, r2, r3, r4, r5, r6, r7,r8, r9)
    return r1, r2, r3, r4, r5, r6, r7, r8, r9

def test_fV(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    r1 = [row9[0], row8[0], row7[0], row6[0], row5[0], row4[0], row3[0], row2[0], row1[0]]
    r2 = [row9[1], row8[1], row7[1], row6[1], row5[1], row4[1], row3[1], row2[1], row1[1]]
    r3 = [row9[2], row8[2], row7[2], row6[2], row5[2], row4[2], row3[2], row2[2], row1[2]]
    r4 = [row9[3], row8[3], row7[3], row6[3], row5[3], row4[3], row3[3], row2[3], row1[3]]
    r5 = [row9[4], row8[4], row7[4], row6[4], row5[4], row4[4], row3[4], row2[4], row1[4]]
    r6 = [row9[5], row8[5], row7[5], row6[5], row5[5], row4[5], row3[5], row2[5], row1[5]]
    r7 = [row9[6], row8[6], row7[6], row6[6], row5[6], row4[6], row3[6], row2[6], row1[6]]
    r8 = [row9[7], row8[7], row7[7], row6[7], row5[7], row4[7], row3[7], row2[7], row1[7]]
    r9 = [row9[8], row8[8], row7[8], row6[8], row5[8], row4[8], row3[8], row2[8], row1[8]]

    col1 = [r1[0], r2[0], r3[0], r4[0], r5[0], r6[0], r7[0], r8[0], r9[0]]
    col2 = [r1[1], r2[1], r3[1], r4[1], r5[1], r6[1], r7[1], r8[1], r9[1]]
    col3 = [r1[2], r2[2], r3[2], r4[2], r5[2], r6[2], r7[2], r8[2], r9[2]]
    col4 = [r1[3], r2[3], r3[3], r4[3], r5[3], r6[3], r7[3], r8[3], r9[3]]
    col5 = [r1[4], r2[4], r3[4], r4[4], r5[4], r6[4], r7[4], r8[4], r9[4]]
    col6 = [r1[5], r2[5], r3[5], r4[5], r5[5], r6[5], r7[5], r8[5], r9[5]]
    col7 = [r1[6], r2[6], r3[6], r4[6], r5[6], r6[6], r7[6], r8[6], r9[6]]
    col8 = [r1[7], r2[7], r3[7], r4[7], r5[7], r6[7], r7[7], r8[7], r9[7]]
    col9 = [r1[8], r2[8], r3[8], r4[8], r5[8], r6[8], r7[8], r8[8], r9[8]]

    t_check(col1, col2, col3, col4, col5, col6, col7, col8, col9)
    return col1, col2, col3, col4, col5, col6, col7, col8, col9

def test_fS(row1, row2, row3, row4, row5, row6, row7, row8, row9):
    r1 = [row1[8], row1[7], row1[6], row1[5], row1[4], row1[3], row1[2], row1[1], row1[0]]
    r2 = [row2[8], row2[7], row2[6], row2[5], row2[4], row2[3], row2[2], row2[1], row2[0]]
    r3 = [row3[8], row3[7], row3[6], row3[5], row3[4], row3[3], row3[2], row3[1], row3[0]]
    r4 = [row4[8], row4[7], row4[6], row4[5], row4[4], row4[3], row4[2], row4[1], row4[0]]
    r5 = [row5[8], row5[7], row5[6], row5[5], row5[4], row5[3], row5[2], row5[1], row5[0]]
    r6 = [row6[8], row6[7], row6[6], row6[5], row6[4], row6[3], row6[2], row6[1], row6[0]]
    r7 = [row7[8], row7[7], row7[6], row7[5], row7[4], row7[3], row7[2], row7[1], row7[0]]
    r8 = [row8[8], row8[7], row8[6], row8[5], row8[4], row8[3], row8[2], row8[1], row8[0]]
    r9 = [row9[8], row9[7], row9[6], row9[5], row9[4], row9[3], row9[2], row9[1], row9[0]]
    t_check(r1, r2, r3, r4, r5, r6, r7,r8, r9)
    return r1, r2, r3, r4, r5, r6, r7, r8, r9

def squarify(i, j, row1, row2, row3, row4, row5, row6, row7, row8, row9):
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

def f_s_board(a):
    row1 = a[0]
    row2 = a[1]
    row3 = a[2]
    row4 = a[3]
    row5 = a[4]
    row6 = a[5]
    row7 = a[6]
    row8 = a[7]
    row9 = a[8]
    b = s_board(row1, row2, row3, row4, row5, row6, row7, row8, row9)
    print(b)
    return

def s_board(r1, r2, r3, r4, r5, r6, r7, r8, r9):
    r = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
    for i in range(0, 9):
        for j in range(0, 9):
            if r[i][j] == 0: r[i][j] = " "
    board = f"""
╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║ {r1[0]} │ {r1[1]} │ {r1[2]} ║ {r1[3]} │ {r1[4]} │ {r1[5]} ║ {r1[6]} │ {r1[7]} │ {r1[8]} ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ {r2[0]} │ {r2[1]} │ {r2[2]} ║ {r2[3]} │ {r2[4]} │ {r2[5]} ║ {r2[6]} │ {r2[7]} │ {r2[8]} ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ {r3[0]} │ {r3[1]} │ {r3[2]} ║ {r3[3]} │ {r3[4]} │ {r3[5]} ║ {r3[6]} │ {r3[7]} │ {r3[8]} ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ {r4[0]} │ {r4[1]} │ {r4[2]} ║ {r4[3]} │ {r4[4]} │ {r4[5]} ║ {r4[6]} │ {r4[7]} │ {r4[8]} ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ {r5[0]} │ {r5[1]} │ {r5[2]} ║ {r5[3]} │ {r5[4]} │ {r5[5]} ║ {r5[6]} │ {r5[7]} │ {r5[8]} ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ {r6[0]} │ {r6[1]} │ {r6[2]} ║ {r6[3]} │ {r6[4]} │ {r6[5]} ║ {r6[6]} │ {r6[7]} │ {r6[8]} ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ {r7[0]} │ {r7[1]} │ {r7[2]} ║ {r7[3]} │ {r7[4]} │ {r7[5]} ║ {r7[6]} │ {r7[7]} │ {r7[8]} ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ {r8[0]} │ {r8[1]} │ {r8[2]} ║ {r8[3]} │ {r8[4]} │ {r8[5]} ║ {r8[6]} │ {r8[7]} │ {r8[8]} ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ {r9[0]} │ {r9[1]} │ {r9[2]} ║ {r9[3]} │ {r9[4]} │ {r9[5]} ║ {r9[6]} │ {r9[7]} │ {r9[8]} ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"""
    return board

def gen_sudoku():
    # Getting original rows
    row1 = test_rows()
    row2 = test_sl(row1, 3)
    row3 = test_sl(row2, 3)
    row4 = test_sl(row3, -1)
    row5 = test_sl(row4, 3)
    row6 = test_sl(row5, 3)
    row7 = test_sl(row6, -1)
    row8 = test_sl(row7, 3)
    row9 = test_sl(row8, 3)

    rrr = random.randrange(80, 800)
    for j in range(1, rrr):
        # Shuffling the rows and columns a random amount of times
        s = ()
        g = (row1, row2, row3, row4, row5, row6, row7, row8, row9)
        rr = random.randrange(10, 31)
        for i in range(1, rr):
            s = testshuffle(g[0], g[1], g[2], g[3], g[4], g[5], g[6], g[7], g[8])
            if i == rr:
                if rr % 2 == 0:
                    g = c(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])
                    row1 = g[0]
                    row2 = g[1]
                    row3 = g[2]
                    row4 = g[3]
                    row5 = g[4]
                    row6 = g[5]
                    row7 = g[6]
                    row8 = g[7]
                    row9 = g[8]
                    break
                else:
                    row1 = s[0]
                    row2 = s[1]
                    row3 = s[2]
                    row4 = s[3]
                    row5 = s[4]
                    row6 = s[5]
                    row7 = s[6]
                    row8 = s[7]
                    row9 = s[8]
                    break
            elif i != rr:
                g = c(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8])

        t_check(row1, row2, row3, row4, row5, row6, row7, row8, row9)
        # print_res((row1, row2, row3, row4, row5, row6, row7, row8, row9))


        # Randomly rotate or flip the rows a random amount of times
        rr = random.randrange(20, 41)
        for i in range(1, rr):
            rf = random.randrange(1, 6)

            if rf == 1:
                e = test_rL(row1, row2, row3, row4, row5, row6, row7, row8, row9)
                row1 = e[0]
                row2 = e[1]
                row3 = e[2]
                row4 = e[3]
                row5 = e[4]
                row6 = e[5]
                row7 = e[6]
                row8 = e[7]
                row9 = e[8]
            elif rf == 2:
                e = test_rR(row1, row2, row3, row4, row5, row6, row7, row8, row9)
                row1 = e[0]
                row2 = e[1]
                row3 = e[2]
                row4 = e[3]
                row5 = e[4]
                row6 = e[5]
                row7 = e[6]
                row8 = e[7]
                row9 = e[8]
            elif rf == 3:
                e = test_rV(row1, row2, row3, row4, row5, row6, row7, row8, row9)
                row1 = e[0]
                row2 = e[1]
                row3 = e[2]
                row4 = e[3]
                row5 = e[4]
                row6 = e[5]
                row7 = e[6]
                row8 = e[7]
                row9 = e[8]
            elif rf == 4:
                e = test_fS(row1, row2, row3, row4, row5, row6, row7, row8, row9)
                row1 = e[0]
                row2 = e[1]
                row3 = e[2]
                row4 = e[3]
                row5 = e[4]
                row6 = e[5]
                row7 = e[6]
                row8 = e[7]
                row9 = e[8]
            elif rf == 5:
                e = test_fV(row1, row2, row3, row4, row5, row6, row7, row8, row9)
                row1 = e[0]
                row2 = e[1]
                row3 = e[2]
                row4 = e[3]
                row5 = e[4]
                row6 = e[5]
                row7 = e[6]
                row8 = e[7]
                row9 = e[8]

    t_check(row1, row2, row3, row4, row5, row6, row7, row8, row9)
    return row1, row2, row3, row4, row5, row6, row7, row8, row9

s = gen_sudoku()

d = diff(s)
print("Done")

#re = remove_numbers([row1, row2, row3, row4, row5, row6, row7, row8, row9])

#f_draw_sudoku(re, 11)





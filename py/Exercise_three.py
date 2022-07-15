"""Exercise 3: ⬤
    *. Bomberman lives in a rectangular grid. Each cell in 
    the grid either contains a bomb or nothing at all.
    Each bomb can be planted in any cell of the grid but once 
    planted, it will detonate after exactly 3 seconds. Once a bomb 
    detonates, it's destroyed — along with anything in its four 
    neighboring cells. This means that if a bomb detonates in cell i, j, 
    any valid cells ( i ± 1, j ) and ( i, j ± 1 )  are cleared. If there is 
    a bomb in a neighboring cell, the neighboring bomb is destroyed without 
    detonating, so there's no chain reaction. Bomberman is immune to bombs, 
    so he can move freely throughout the grid. Here's what he does:

    1.     Initially, Bomberman arbitrarily plants bombs in some of the cells,
    the initial state.
    2.     After one second, Bomberman does nothing.
    3.     After one more second, Bomberman plants bombs in all cells without 
    bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
    4.     After one more second, any bombs planted exactly three seconds ago will detonate.
    Here, Bomberman stands back and observes.
    5.     Bomberman then repeats steps 3 and 4 indefinitely.
    Note that during every second Bomberman plants bombs, the bombs are planted 
    simultaneously (i.e., at the exact same moment), and any bombs planted at the 
    same time will detonate at the same time.

    *. Given the initial configuration of the grid with the locations of Bomberman's 
    first batch of planted bombs, determine the state of the grid after N seconds.
    For example, if the initial grid looks like:
        . . .
        . O .
        . . .
    It looks the same after the first second. After the second second, Bomberman 
    has placed all his charges:
        O O O
        O O O
        O O O
    At the third second, the bomb in the middle blows up, emptying all surrounding cells:
        O.O
        ...
        O.O

        *. Function Description
        Create the bomber_man function with following parameter(s):
        ●       int n: the number of seconds to simulate
        ●       string grid[r]: an array of string that represents the grid
        Returns
    	●	string[r]: n array of string that represent the grid in its final state

        Sample Input:
        3
        . . . . . . .
        . . . O . . .
        . . . . O . .
        . . . . . . .
        O O . . . . .
        O O . . . . .

        Sample Output
        O O O . O O O
        O O . . . O O
        O O O . . . O
        . . O O . O O
        . . . O O O O
        . . . O O O O
"""

from time import  sleep

def increment_time(grid,grid_times):
    for i,row in enumerate(grid):
        for j,grid_item in enumerate(row):
            if grid[i][j] == 'O':
                grid_times[i][j] += 1
    
            if grid_times[i][j] == 3:
            
                if grid_item == 'O' and i != 0 and i != len(grid)-1 \
                    and j != 0 and j != len(row)-1:
                    grid[i+1][j] = '.'
                    grid[i][j-1] = '.'
                    grid[i][j+1] = '.'
                    grid[i-1][j] = '.'

                elif grid_item == 'O' and i == 0:
                    if j == 0:
                        grid[i][j+1] = '.'
                        grid[i+1][j] = '.'  
                    elif j == len(row)-1:
                        grid[i][j-1] = '.'
                        grid[i+1][j] = '.'
                    else:
                        grid[i][j+1] = '.'
                        grid[i][j-1] = '.'
                        grid[i+1][j] = '.'

                elif grid_item == 'O' and i == len(grid)-1:
                    if j == 0:
                        grid[i][j+1] = '.'
                        grid[i-1][j] = '.'  
                    elif j == len(row)-1:
                        grid[i][j-1] = '.'
                        grid[i-1][j] = '.'
                    else:
                        grid[i][j+1] = '.'
                        grid[i][j-1] = '.'
                        grid[i-1][j] = '.'  


                elif grid_item == 'O' and j == 0 and i != 0:
                    grid[i][j+1] = '.'
                    grid[i-1][j] = '.'
                    grid[i+1][j] = '.'

                elif grid_item == 'O' and j == len(row)-1 and i != len(grid)-1:
                    grid[i][j-1] = '.'
                    grid[i-1][j] = '.'
                    grid[i+1][j] = '.'

                grid[i][j] = '.'
                grid_times[i][j] = 0


def bomber_man(n,grid):
    print("please wait for a few seconds!")
    grid_times = [[int(0) for x in range(len(grid[1]))] for y in range(len(grid))]
    while True:
        #first second
        sleep(1)
        increment_time(grid,grid_times)            
        n -= 1
        #second second
        sleep(2)
        n -= 1
        for i,row in enumerate(grid):
            for j,grid_item in enumerate(row): 
                if grid[i][j] == '.':
                    grid[i][j] = 'O'
        increment_time(grid,grid_times)
        #third second
        sleep(3)
        n -= 1
        increment_time(grid,grid_times)
        if(n <= 0):
            break

    return grid

def print_2d_grid(grid_list):
    print("\n")
    for i in range(len(grid_list)):
        for j in range(len(grid_list[i])):
            print(f"{grid_list[i][j]} ", end=" ")
        print()
    print("\n")


n = input("enter n: ")
print("\n")
grid_list = []
while True:
    string = input()
    string = "".join(string.split())
    if string == "":
        break

    string = list(string)
    grid_list.append(string)

print_2d_grid(grid_list)

result_grid_list = bomber_man(n,grid_list)

print_2d_grid(result_grid_list)

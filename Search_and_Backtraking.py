from Constraint_Propagation import *

def search(values):
    "Using depth-first search and propagation, try all possible values."

    values = reduce_puzzle(values)#reduce the puzzle
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values ## Solved!

    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)## Choose the unfilled squares with the least possibilities

    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt




#EXAMPLES
#display(search(grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')))

#display(search(grid_values('....8....8.9.71.2.4.35....1...1....7..2.34.8.73...9..49.....7.2..82.5.9.1...4.3..')))

#display(search(grid_values('8..........36......7..9.2...5...7.......457.....1...3...1....68..85...1..9....4..')))
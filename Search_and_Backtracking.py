from Constraint_Propagation import *


def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."

    values = reduce_puzzle(values)#reduce the puzzle

    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)# Choose the unfilled squares with the fewest possibilities


    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    while bool(values) :
        for i in values[s]:
            values[s] = i
            search(values)
            values[s] = str(i + values[s])





display(search(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))
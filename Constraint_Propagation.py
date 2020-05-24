
from Function_only_choice import *


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])#No. of solved box before applying strategies

        values = eliminate(values)#Elimination Strategy

        values = only_choice(values)#only choice Strategy
 
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])#No. of solved box after applying strategies

        stalled = solved_values_before == solved_values_after# If no new values were added, stop the loop.

        if len([box for box in values.keys() if len(values[box]) == 0]):#return False if there is a box with zero available values:
            return False
    return values



#Examples
#display(reduce_puzzle(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))
#display(eliminate(grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')))
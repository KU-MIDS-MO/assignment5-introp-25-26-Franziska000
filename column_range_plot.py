##task1

#Write a function `column_range_plot(A, filename="column_ranges.pdf")` that;

#- receives a 2D NumPy array `A`,
#- computes the range (maximum minus minimum) of each column, (Spannweite (Range) Range = Maximum -- Minimum)
#- create a bar plot showing the ranges of all columns, (Balkendiagramm, in dem die 
    # Spannweiten aller Spalten dargestellt werden; jede Spalte bekommt einen eigenen Balken)
#- saves the plot as a PDF file,
#- and returns a 1D NumPy array containiing the column ranges. (1D array, das die Spannweiten aller Spalten enthält)

import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [5, 11, 15, 20],
    [7, 50, 45, 3]
    ])

print(A)

def column_range_plot(A, filename="column_ranges.pdf"):
    A = np.asarray(A)
    
    if A.ndim != 2:
        return 0
    
    ranges = []
    
    num_rows, num_cols = A.shape
    
    for col in range(num_cols):
        
        column = A[:, col]
        
        num_min = column[0]
        for i in range(1, len(column)):
            if num_min <= column[i]:
                continue
            else:
                num_min = column[i]

        num_max = column[0]
        for i in range(1, len(column)):
            if num_max >= column[i]:
                continue
            else:
                num_max = column[i]

        print("row", col, "min:", num_min, "max:", num_max)

        ranges.append(num_max - num_min)
    
    ranges = np.array(ranges)
        
    plt.bar(range(len(ranges)), ranges)
    plt.title("Ranges of Columns")
    plt.xlabel("Column")
    plt.ylabel("Range")
    
    plt.savefig(filename)
    plt.close()
        
    return ranges

    pass

print(column_range_plot(A))


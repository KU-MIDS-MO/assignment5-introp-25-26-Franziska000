##task2

#Write a function `detect_turning_points(signal, filename="turning_points.pdf")` that:

#- receives a 1D NumPy array representing a signal
#- identifies all indices where the direction of the signal changes  
#  (i.e., where the discrete difference changes sign),
#- plots the signal and mark these turning points,
#- saves the figure as a PDF file,
#- and returns a NumPy array containing the indices of the detected points

#Ich gebe ein 1D-NumPy-Array signal ein, also eine Liste
#Einen Wendepunkt im Signal ist ein Punkt, wo sich die Richtung ändert, z.B. 1, 3, 2, 5, 4 -> Wendepunkt an Index 1 und 3
#plt.plot(signal) und Wendepunkt markieren mit z.B. rotem Punkt plt.scatter
#Und ich speichere dann als pdf und gebe Array mit Indizes der Wendepunkte zurück


import numpy as np
import matplotlib.pyplot as plt

signal = np.array([5, 11, 30, 20])

print(signal)

def detect_turning_points(signal, filename="turning_points.pdf"):
    signal = np.asarray(signal)
    
    diffs = np.diff(signal)
    turning_points = []
    
    for i in range(len(diffs)-1):
        a = diffs[i]
        b = diffs[i+1]
        
        if a > 0 and b < 0:
            turning_points.append(i+1)
        elif a < 0 and b > 0:
            turning_points.append(i+1)
            
    turning_points = np.array(turning_points)
    
    plt.plot(signal, label = "Signal")
    plt.scatter(turning_points, signal[turning_points],
                color = "red", label = "Turning Point")
    plt.title("Detected Turning Points")
    plt.savefig(filename)
    
    return turning_points
    pass

print(detect_turning_points(signal, filename="turning_points.pdf"))

"""
Graph Plotter
author: Noah Kattner
date: 4/24/2025
"""

import math
import matplotlib.pyplot as plot


class Main:
    def __init__(self):
        self.angles = range(360)
        self.x_values = [math.cos(math.radians(angle)) for angle in self.angles]
        self.y_values = [math.sin(math.radians(angle)) for angle in self.angles]

        self.graph_circle()


    def graph_circle(self):
        plot.figure(figsize=(15, 8))
        plot.plot(self.x_values, self.y_values, label = "Circle", linewidth = 2, linestyle = "-", color = "blue")
        plot.title("Circumference of a Circle")
        plot.xlabel("Cosine")
        plot.ylabel("Sine")
        plot.grid(True)
        plot.axis('equal')
        plot.legend()
        plot.show()


if __name__ == '__main__':
    Main()
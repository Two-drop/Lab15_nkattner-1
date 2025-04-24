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

        # graph_circle()



if __name__ == '__main__':
    Main()
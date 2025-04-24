"""
Graph Plotter
author: Noah Kattner
date: 4/24/2025
"""

import math
import matplotlib.pyplot as plot


class Main:
    """Main class to run the program
    """
    def __init__(self):
        """ Initializes basic values to use to graph a circle
        """
        self.angles = range(360)
        self.x_values = [math.cos(math.radians(angle)) for angle in self.angles]
        self.y_values = [math.sin(math.radians(angle)) for angle in self.angles]
        self.t_values = [i * 0.01 for i in range(0, int(2 * math.pi / 0.01))]

        self.graph_heart()
        # self.graph_circle()

    def graph_heart(self):
        """ Function that will graph a red heart
        """
        x_values = [16 * math.sin(t)**3 for t in self.t_values]
        y_values = [
            (13 * math.cos(t)) - (5 * math.cos(2 * t)) - (2 * math.cos(3 * t))
            - math.cos(4 * t) for t in self.t_values
        ]

        plot.figure(figsize=(8, 6))
        plot.fill(x_values, y_values, color='red', alpha=0.7)
        plot.plot(x_values, y_values, color='red')
        plot.title('Heart')
        plot.axis('equal')
        plot.show()
    
    def graph_circle(self):
        """ Function that will graph the circle
        """
        plot.figure(figsize=(10, 7))
        plot.plot(self.x_values, self.y_values, linewidth = 2, linestyle = "-", color = "blue")
        plot.title("Circumference of a Circle")
        plot.xlabel("Cosine")
        plot.ylabel("Sine")
        plot.grid(True)
        plot.axis('equal')
        plot.show()



if __name__ == '__main__':
    Main()
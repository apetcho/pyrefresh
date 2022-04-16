#!/usr/bin/env python3
import tkinter as tk
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class VonKoch:

    def __init__(self):
        self.currentPoint = None
        self.angle = 0.0
        self.point = Point(0, 0)
        window = tk.Tk()
        window.title("Von Koch snowflake")
        self.canvas = tk.Canvas(window, width=600, height=400)
        self.canvas.config(background="yellow")
        self.canvas.pack()

        frame = tk.Frame(window);
        frame.pack()
        self.level = tk.StringVar(value="4")
        self.side = tk.StringVar(value="200")
        tk.Label(frame, text="Level").pack(side=tk.LEFT)
        tk.Entry(frame, textvariable=self.level).pack(side=tk.LEFT)
        tk.Label(frame, text=self.side).pack(side=tk.LEFT)
        tk.Button(frame, text="draw", command=self.display).pack(side=tk.LEFT)
        window.mainloop()

    def _right(self, x):
        pass

    def _left(self, x):
        pass

    def _draw_four_lines(self, side, level):
        pass

    def display(self):
        pass


def main():
    VonKoch()


if __name__ == "__main__":
    main()

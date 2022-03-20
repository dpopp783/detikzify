'''
Module holding distance functions that can be used by different Node Types
'''

from Point import Point

class Distances:
    @staticmethod
    def ManhattanDistance(a: Point, b: Point):
        return (a.x - b.x, a.y - b.y)
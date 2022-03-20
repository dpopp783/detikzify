'''
Module holding distance functions that can be used by different Node Types
'''
# TODO change to PygameCoord
from tikz_elements.TikzCoord import TikzCoord

class Distances:
    @staticmethod
    def ManhattanDistance(a: TikzCoord, b: TikzCoord):
        return (a.x - b.x, a.y - b.y)
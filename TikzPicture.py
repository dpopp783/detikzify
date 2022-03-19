from typing import List

from NodeType import NodeType
from TikzNode import TikzNode
from Point import Point

class TikzPicture:

    params: List[List[str]] = []
    node_types: List[NodeType] = []
    nodes: List[TikzNode] = []

    def __init__(self):
        pass

    def add_node_type(self, nt: NodeType):
        self.node_types.append(nt)

    def add_node(self, node: TikzNode):
        self.nodes.append(node)





from typing import List

from tikz_elements.NodeType import NodeType
from tikz_elements.TikzNode import TikzNode
from tikz_elements.Line import Line


class TikzPicture:

    params: List[List[str]] = []
    node_types: List[NodeType] = []
    nodes: List[TikzNode] = []
    lines: List[Line] = []

    def __init__(self):
        pass

    def add_node_type(self, nt: NodeType):
        self.node_types.append(nt)

    def add_node(self, node: TikzNode):
        self.nodes.append(node)

    def add_line(self, line: Line):
        self.lines.append(line)




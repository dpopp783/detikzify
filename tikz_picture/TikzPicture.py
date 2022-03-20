from typing import List

from tikz_elements.NodeStyle import NodeStyle
from tikz_elements.TikzNode import TikzNode
from tikz_elements.Line import Line


class TikzPicture:

    params: List[List[str]] = []
    node_styles: List[NodeStyle] = []
    nodes: List[TikzNode] = []
    lines: List[Line] = []

    def __init__(self):
        pass

    def add_node_style(self, style: NodeStyle):
        self.node_styles.append(style)

    def add_node(self, node: TikzNode):
        self.nodes.append(node)

    def add_line(self, line: Line):
        self.lines.append(line)




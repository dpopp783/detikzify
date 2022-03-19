from typing import List
from TikzPicture import TikzPicture

class TikzPictureCodeGenerator:

    picture: TikzPicture
    code: List[str]

    def __init__(self, picture: TikzPicture):
        self.picture = picture
        self.code = []

    def generate_tikz_code(self) -> str:

        self.code.append("\\begin{tikzpicture}")

        # TODO add specifications

        # add code for node type style definitions
        for nt in self.picture.node_types:
            self.code.append(nt.tikz_code())

        # add code for each node
        for node in self.picture.nodes:
            self.code.append(node.tikz_code())

        # TODO add code for edges

        self.code.append("\\end{tikzpicture}")
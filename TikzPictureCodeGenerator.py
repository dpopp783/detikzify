from typing import List
from TikzPicture import TikzPicture

class TikzPictureCodeGenerator:

    picture: TikzPicture
    libraries = set()
    code: List[str]

    def __init__(self, picture: TikzPicture):
        self.picture = picture
        self.code = []

    def generate_tikz_code(self) -> List[str]:

        # TODO fix double backslash, for some reason escape character isn't working
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

        return self.code

    def create_tex_file(self, file_name: str):
        self.add_tex_boilerplate()

        with open(file_name, "w") as tex_file:
            for line in self.code:
                tex_file.write(line)
                tex_file.write("\n")


    def add_tex_boilerplate(self):

        self.code.insert(0, "\\begin{document}")
        self.code.append("\\end{document}")

        ## TODO add line for tikzpackage imports

        self.code.insert(0, "\\usepackage{tikz}")
        self.code.insert(0, "\\documentclass{article}")


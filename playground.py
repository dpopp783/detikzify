from TikzNode import TikzNode
from NodeType import NodeType
from Point import Point
from TikzPicture import TikzPicture
from TikzPictureCodeGenerator import TikzPictureCodeGenerator

if __name__ == "__main__":

    cnode: NodeType = NodeType("cnode", "circle", [[]])

    node: TikzNode = TikzNode(cnode, "a", [["label","below:x"]], Point(2,3))

    picture: TikzPicture = TikzPicture()
    picture.add_node_type(cnode)
    picture.add_node(node)

    generator: TikzPictureCodeGenerator = TikzPictureCodeGenerator(picture)
    code = generator.generate_tikz_code()

    for line in code:
        print(line)
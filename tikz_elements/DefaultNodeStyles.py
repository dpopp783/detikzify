from typing import List

from tikz_elements.NodeStyle import NodeStyle

class DefaultNodeStyles:

    default_node_styles: List[NodeStyle] = []

    cnode_small: NodeStyle = NodeStyle("cnode_small", "circle", 0.5)
    cnode_med: NodeStyle = NodeStyle("cnode_med", "circle", 1)
    cnode_large: NodeStyle = NodeStyle("cnode_large", "circle", 1.5)

    sqnode_small: NodeStyle = NodeStyle("sqnode_small", "square", 0.5)
    sqnode_med: NodeStyle = NodeStyle("sqnode_med", "square", 1)
    sqnode_large: NodeStyle = NodeStyle("sqnode_large", "square", 1.5)

    default_node_styles.append(cnode_small)
    default_node_styles.append(cnode_med)
    default_node_styles.append(cnode_large)
    default_node_styles.append(sqnode_small)
    default_node_styles.append(sqnode_med)
    default_node_styles.append(sqnode_large)
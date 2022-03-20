from typing import List

from tikz_elements.NodeType import NodeType

class DefaultNodeTypes:

    default_node_types: List[NodeType]

    cnode_small: NodeType = NodeType("cnode_small", "circle", 0.5)
    cnode_med: NodeType = NodeType("cnode_med", "circle", 1)
    cnode_large: NodeType = NodeType("cnode_large", "circle", 1.5)

    sqnode_small: NodeType = NodeType("sqnode_small", "square", 0.5)
    sqnode_med: NodeType = NodeType("sqnode_med", "square", 1)
    sqnode_large: NodeType = NodeType("sqnode_large", "square", 1.5)

    default_node_types.append(cnode_small)
    default_node_types.append(cnode_med)
    default_node_types.append(cnode_large)
    default_node_types.append(sqnode_small)
    default_node_types.append(sqnode_med)
    default_node_types.append(sqnode_large)
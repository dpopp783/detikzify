from typing import List

class TikzNode:

    node_type: str
    params: dict[str,str]

    def __init__(self, nt: str, *params: List[List[str]] ):
        self.node_type = nt

        self.params = dict()
        for keyword, value in params:
            params[keyword] = value
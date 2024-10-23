import logging
from typing import List
from langgraph.graph import  StateGraph

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GraphBuilder:
    def __init__(
        self,
        state,
        nodes: dict,
        edges: List[dict],
        entrypoint: str
    ):
        """Builders langgraph for provided nodes and edges.

        Args:
            state (BaseModel): the state assigned to the graph
            nodes (dict): Its of the following structure {"name": node_func}
            edges (dict): Its of the following structure {"from": "name_of_node", "condition": condition_func or None, "to": {"condtion1": "to_node" , ...}}
            entrypoint (str): Name of node that is the entrypoint for the graph
        """
        self.state = state
        self.nodes = nodes
        self.edges = edges
        self.entrypoint = entrypoint
        
    def build_graph(self):
        buidler = StateGraph(self.state)
        
        for node_name, node_func in self.nodes.items():
            buidler.add_node(node_name, node_func)
        
        for edge in self.edges:
            if not edge["condition"]:
                buidler.add_edge(edge["from"], edge["to"]) 
            else:
                buidler.add_conditional_edges(
                    edge["from"],
                    edge["condition"],
                    edge["to"]
                )
        buidler.set_entry_point(self.entrypoint)
        
        return buidler.compile()
    
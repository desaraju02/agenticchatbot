
from typing_extensions import List, TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated


class State(TypedDict):
    """
    Represent the structure of the state used in the graph.
    """
    message: Annotated[List, add_messages]
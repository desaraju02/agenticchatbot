from src.langgraphagenticai.state.state import State
from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
       self.llm = model
       self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
            Build a basic chatbot graph structure using Langgraph.
            This method initializes a chatbot node using the BasicChatbot Node class
            and integrated it into the graph structure.
            The  chatbot node  is set as both the enntry and exit point of the graph.
        """
        print("Building Basic Chatbot node...")
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        print("Basic Chatbot graph built successfully.")

    def setup_graph(self, usecase: str):
        """
            Setup the graph based on the selected use case.
            Currently supports only "Basic ChatBot" use case.
        """
        if usecase == "Basic Chatbot":
            print("Setting up Basic Chatbot graph...")
            self.basic_chatbot_build_graph()
            return self.graph_builder.compile()
        else:
            raise ValueError(f"Unsupported use case: {usecase}")